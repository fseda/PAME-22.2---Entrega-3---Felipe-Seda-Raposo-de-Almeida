from Models.Consultor import Consultor
from Models.Gerente import Gerente
from Models.Projeto import Projeto

from constants import OK, NOT_LOGGED_IN, USERNAME_EXISTS, MANAGER_HAS_ACTIVE_PROJECTS,\
    WRONG_PASSWORD, UNAUTHORIZED, FAILED, USER_DOES_NOT_EXIST, USER_ALREADY_IN_PROJECT,\
    PROJECT_DOES_NOT_EXIST

class Sistema:
    def __init__(self):
        self.users: list[Gerente | Consultor] = [] # Lista de Usuários
        self.projects: list[Projeto] = [] # Lista de Projetos

        self.logged_in_user: Gerente | Consultor = None

    # A
    def create_user(self, username, password, role):
        if self.username_exists(username):
            return USERNAME_EXISTS

        id = len(self.users) + 1

        if role == 0:
            self.users.append(Gerente(id=id, username=username, password=password))
        else:
            self.users.append(Consultor(id=id, username=username, password=password))
        
        return OK
    
    # A
    def delete_user(self, username, role):
        if role == 0:
            role = Gerente
        elif role == 1:
            role = Consultor

        for user in self.users:
            if user.username == username and isinstance(user, role):

                # Se o usuario for gerente e ainda tiver projetos ativos
                # nao poderá ser removido
                
                if role == Gerente and len(self.get_projects_by_username(username)) != 0:
                    return MANAGER_HAS_ACTIVE_PROJECTS

                self.users.remove(user)  
                return OK  
        
        return USER_DOES_NOT_EXIST

    # A
    def get_users_by_role(self, role) -> Gerente | Consultor:
        users_by_role = []

        if role == 0:
            role = Gerente
        else:
            role = Consultor
        
        for user in self.users:
            if isinstance(user, role):
                users_by_role.append({'id': user.id, 'username': user.username})
        return users_by_role

    # G | C
    def get_user_data(self):
        if not self.logged_in():
            return NOT_LOGGED_IN

        for user in self.users:
            if user.username == self.logged_in_user.username:
                return user

    # A
    def create_project(self, name, type_of_project, manager, consultants):
        id = len(self.projects) + 1
        project = Projeto(id, name, type_of_project, manager, consultants)
        self.projects.append(project)
        return OK

    # A
    def delete_project(self, id):
        for project in self.projects:
            if project.id == id:
                self.projects.remove(project)
                return OK
        return PROJECT_DOES_NOT_EXIST
    
    # G
    def allocate_consultant_to_project(self, project_id, consultant):
        if not self.logged_in():
            return NOT_LOGGED_IN
        
        if not isinstance(self.logged_in_user, Gerente):
            return UNAUTHORIZED

        for user in self.users:
            if isinstance(user, Consultor) and user.username == consultant:
                break
            return USER_DOES_NOT_EXIST

        for project in self.projects:
            if consultant in project.consultants:
                return USER_ALREADY_IN_PROJECT

            if project.id == project_id:
                project.consultans.append(consultant)
                return OK

    # A
    def get_projects(self):
        return self.projects

    # A
    def get_projects_by_username(self, username) -> list[Projeto]:
        projects = []

        for project in self.projects:
            if project.manager == username:
                projects.append(project)
            elif username in project.consultants:
                projects.append(project)
        return projects

    # G
    def get_projects_with_advance_requests(self):
        if not self.logged_in():
            return NOT_LOGGED_IN
        
        if not isinstance(self.logged_in_user, Gerente):
            return UNAUTHORIZED

        list_of_projects = []
        for project in self.projects:
            if project.manager == self.logged_in_user.username and project.advance_project_request['Requested']:
                list_of_projects.append(project)
        
        return list_of_projects
                    
    # G
    def decide_advance_project_request(self, project_id, decision):
        if not self.logged_in():
            return NOT_LOGGED_IN
        
        if not isinstance(self.logged_in_user, Gerente):
            return UNAUTHORIZED
        
        for project in self.projects:
            if project.id == project_id:
                return project.advance_project(decision)    

        return FAILED    

    def get_project_by_id(self, project_id) -> Projeto:
        for project in self.projects:
            if project.id == project_id:
                return project
        return PROJECT_DOES_NOT_EXIST

    # G
    def transfer_project_to_another_manager(self, project_id, new_manager):
        if not self.logged_in():
            return NOT_LOGGED_IN
        
        if not isinstance(self.logged_in_user, Gerente):
            return UNAUTHORIZED

        for project in self.projects:
            if project.id == project_id:
                project.manager = new_manager
                return OK
        return FAILED
        
    # C
    def create_quit_project_request(self, project_id):
        if not self.logged_in():
            return NOT_LOGGED_IN
        
        if not isinstance(self.logged_in_user, Consultor):
            return UNAUTHORIZED

        project_manager = ''
        for project in self.projects:
            if project.id == project_id:
                project_manager = project.manager

                # Prosseguir apenas se usuario está alocado no projeto
                for consultant in project.consultants: 
                    if consultant == self.logged_in_user:
                        for manager in self.users:
                            if isinstance(manager, Gerente):
                                if manager.username == project_manager:
                                    return manager.quit_project(project_id, self.logged_in_user)
                return UNAUTHORIZED
                
        

        return FAILED

    # G
    def get_projects_with_quit_requests(self):
        if not self.logged_in():
            return NOT_LOGGED_IN
        
        if not isinstance(self.logged_in_user, Gerente):
            return UNAUTHORIZED

        return self.logged_in_user.quit_projects_requests

    # G
    def decide_quit_project_request(self, project_id, consultant, decision):
        if not self.logged_in():
            return NOT_LOGGED_IN
        
        if not isinstance(self.logged_in_user, Gerente):
            return UNAUTHORIZED
        
        request = {
            'Projeto ID': project_id,
            'Consultor': consultant
        }

        # Se a decisao de retirar consultor do projeto nao for aceita
        # retirar pedido
        if not decision:
            self.logged_in_user.quit_projects_requests.remove(request)
            return OK

        # Se a decisao for aceita, tirar consultor do projeto
        self.projects.consultants.remove(consultant)
        self.logged_in_user.quit_projects_requests.remove(request)

        return OK
    
    # G
    def submit_project(self, project_id):
        if not self.logged_in():
            return NOT_LOGGED_IN
        
        if not isinstance(self.logged_in_user, Gerente):
            return UNAUTHORIZED
                
        for project in self.projects:
            if project.id == project_id:
                self.projects.remove(project)
                return OK
        
        return FAILED

    def username_exists(self, username):
        for user in self.users:
            if user.username == username:
                return True
        return False

    def logged_in(self) -> bool:
        return not self.logged_in_user == None

    # A
    def login(self, username, password) -> int:
        for user in self.users:
            # Usuario existe
            if user.username == username:
                if user.password == password:
                    self.logged_in_user = user
                    return OK # Usuario digitou a senha corretamente (logged in)
                else: 
                    return WRONG_PASSWORD # Senha incorreta
             
        return USER_DOES_NOT_EXIST # Usuario nao existe
    
    # G | C
    def logout(self):
        self.logged_in_user = None

    # A
    def quit(self):
        pass
    
               