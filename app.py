from Models.Sistema import Sistema
from Models.Consultor import Consultor
from Models.Gerente import Gerente
from Models.Projeto import Projeto

from constants import OK, FAILED, NOT_LOGGED_IN, USERNAME_EXISTS,\
    WRONG_PASSWORD, USER_DOES_NOT_EXIST, UNAUTHORIZED,\
    PROJECT_ADVANCE_ALREADY_REQUESTED, CONSULTANT_NOT_IN_PROJECT,\
    MANAGER_HAS_ACTIVE_PROJECTS, DES, CON, IDV, PROJECT_DOES_NOT_EXIST,\
    NOT_ADVANCED

import os

def show_options(sys, role):

    if role == -1:
        print(' 1 - Login')
    else:
        print(' 1 - Logout')
    
    print()
    print(' 2 - Criar Gerente')
    print(' 3 - Deletar Gerente')
    print(' 4 - Listar Gerentes')
    print()
    print(' 5 - Criar Consultor')
    print(' 6 - Deletar Consultor')
    print(' 7 - Listar Consultores')
    print()
    print(' 8 - Criar Projeto')
    print(' 9 - Deletar Projeto')
    print('10 - Listar Projetos')
    print()

    if role == 0 or role == 1:
        show_logged_in_options()
    if role == 0:
        show_manager_options()
    elif role == 1:
        show_consultant_options()

    print(' 0 - Sair do Programa')
    print(' ENTER - Limpar Tela')
    print()

def show_logged_in_options():
    print('11 - Ver Dados do Usuário')
    print('12 - Alterar Dados do Usuário')
    print('13 - Listar Seus Projetos')
    print('14 - Avançar Com Projeto')

def show_manager_options():
    print('15 - Pedidos De Retirada')
    print('16 - Passar Projeto Para Outro Gerente')
    print('17 - Entregar Projeto')
    print()

def show_consultant_options():
    print('15 - Sair De Projeto')
    print()

def get_options(sys: Sistema, role, op):

    match op:
        case '2': # Criar Gerente
            print('---------- Criar Gerente ----------')
            username = input('Usuário: ')
            password = input('Senha: ')

            if sys.create_user(username, password, 0) == OK:
                print()
                print('Sucesso!')
                print('----------------------------\n')

                return
            
            else:
                print('Esse Usuário já existe.')
                print('----------------------------\n')

        case '3': # Remover Gerente
            print('---------- Remover Gerente ----------')
            username = input('Digitar Usuário do Gerente: ')
            print()
            res = sys.delete_user(username, 0)
            
            if res == OK:
                print('Gerente foi removido com sucesso!')
            elif res == MANAGER_HAS_ACTIVE_PROJECTS:
                print('Gerente está com projeto em andamento. Não poderá ser removido.')
                print('----------------------------\n')
            elif res == USER_DOES_NOT_EXIST:
                print('Esse Gerente não existe.')
                print('----------------------------\n')

            return
        
        case '4': # Listar Gerentes
            print('---------- Listar Gerentes ----------')
            
            managers = sys.get_users_by_role(0)
            if len(managers) == 0:
                print('Não há gerentes cadastrados.')
                print('----------------------------\n')
                return

            print('ID | Usuário')
            for manager in managers:
                print(f'{manager["id"]} | {manager["username"]}')
            print('----------------------------\n')

            return
        
        case '5': # Criar Consultor
            print('---------- Criar Consultor ----------')
            username = input('Usuário: ')
            password = input('Senha: ')

            if sys.create_user(username, password, 1) == OK:
                print()
                print('Sucesso!')
                print('----------------------------\n')
            else:
                print('Esse Usuário já existe.')
                print('----------------------------\n')

            return

        case '6': # Remover Consultor
            print('---------- Remover Consultor ----------')
            username = input('Digitar Usuário do Consultor: ')
            print()
            res = sys.delete_user(username, 1)
            
            if res == OK:
                print('Consultor foi removido com sucesso!')
            if res == USER_DOES_NOT_EXIST:
                print('Esse Consultor não existe.')
                print('----------------------------\n')
            return

        case '7': # Listar Consultores
            print('---------- Listar Consultores ----------')
            
            consultants = sys.get_users_by_role(1)
            if len(consultants) == 0:
                print('Não há consultores cadastrados.')
                print('----------------------------\n')
                return

            print('ID | Usuário')
            for consultant in consultants:
                print(f'{consultant["id"]} | {consultant["username"]}')
            print('----------------------------\n')
            return

        case '8': # Criar Projeto
            print('---------- Criar Projeto ----------')
            project_name = input('Nome do Projeto (0 para cancelar): ')
            if project_name == '':
                print('Nome Invalido')
                print('----------------------------\n')
                return

            if project_name == '0':
                print('Operação Cancelada.')
                print('----------------------------\n')
                return

            project_type = input('Tipo do Projeto\n\
1 - Desenvolvimento\n\
2 - Concepção\n\
3 - Identidade Visual\n\
Digite: ')
            if project_type == '1':
                project_type = DES
            elif project_type == '2':
                project_type = CON
            elif project_type == '3':
                project_type = IDV
            else:
                print('Opção Invalida')
                print('----------------------------\n')
                return

            project_manager = input('Gerente do Projeto: ')
            if project_manager == '':
                print('Gerente Invalido')
                print('----------------------------\n')
                return

            managers = sys.get_users_by_role(0)
            for manager in managers:
                if manager['username'] == project_manager:
                    print('Adicionar Consultores')

                    consultants = set()
                    while True:
                        consultant = input('Digite o nome de um Consultor (ENTER para concluir): ')
                        if consultant == '':
                            break
                        for c in sys.get_users_by_role(1):
                            if consultant == c['username']:
                                if consultant not in consultants:
                                    consultants.add(consultant)
                                    break
                                print('Esse Consultor já está no projeto.')
                        
                        consultants.add(consultant)

                    sys.create_project(project_name, project_type, project_manager, consultants)
                    print('Sucesso!')
                    print('----------------------------\n')
                    return

            print()
            print('Esse Gerente não existe.')   
            print('----------------------------\n')

            return
                
        case '9': # Deletar Projeto
            print('---------- Deletar Projeto ----------')
            project_id = input('ID do Projeto que deseja deletar: ')
            
            res = sys.delete_project(project_id)
            if res == OK:
                print('Projeto Deletado!')
                print('----------------------------\n')
            elif res == PROJECT_DOES_NOT_EXIST:
                print('Projeto não encontrado.')
                print('----------------------------\n')
            return

        case '10': # Listar Projetos
            print('---------- Listar Projetos ----------')
            
            projects = sys.get_projects()
            if len(projects) == 0:
                print('Não há projetos cadastrados.')
                print('----------------------------\n')
                return

            print('ID | Nome do Projeto | Tipo de Projeto | Etapas Restantes | Gerente | # de Consultores\n')
            for project in projects:
                if project.type_of_project == DES:
                    type_of_project = 'Desenvolvimento'
                elif project.type_of_project == CON:
                    type_of_project = 'Concepção'
                elif project.type_of_project == IDV:
                    type_of_project = 'Identidade Visual'
                print(f'{project.id} | {project.name} | {type_of_project} | {project.remaining_steps} | {project.manager} | {len(project.consultants)}')
            print('----------------------------\n')
            
            return

    if role == 0 or role == 1:
        match op:
            case '11': # Ver Dados Do Usuário
                print('---------- Dados do Usuário ----------')
                if role == 0:
                    role_2 = 'Gerente'
                else:
                    role_2 = 'Consultor'

                id = sys.logged_in_user.id
                username = sys.logged_in_user.username
                password = sys.logged_in_user.password

                print(f'ID: {id}')
                print(f'Usuário: {username}')
                print(f'Senha: {password}')
                print(f'Cargo: {role_2}')
                print('----------------------------\n')
                return

            case '12': # Alterar  Dados Usuário
                print('---------- Alterar Dados do Usuário ----------')
                username = input('Novo Usuário: ')
                password = input('Nova Senha: (Para manter mesma senha basta pressionar ENTER): ')

                if sys.username_exists(username):
                    print('Esse Usuário já existe.')
                    print('----------------------------\n')
                    return

                for user in sys.users:
                    if user.username == sys.logged_in_user.username:
                        user.username = username
                        if not password == '':
                            user.password = password
                        
                        print('Sucesso!')
                        print('----------------------------\n')
                        return
           
            case '13': # Listar Projetos Do Usuário
                print(f'---------- Projetos do Usuário {sys.logged_in_user.username} ----------')
                projects = sys.get_projects_by_username(sys.logged_in_user.username)

                if len(projects) == 0:
                    print('Não há projetos cadastrados.')
                    print('----------------------------\n')
                    return

                print('ID | Nome do Projeto | Tipo de Projeto | Etapas Restantes | Gerente | # de Consultores\n')
                for project in projects:
                    if project.type_of_project == DES:
                        type_of_project = 'Desenvolvimento'
                    elif project.type_of_project == CON:
                        type_of_project = 'Concepção'
                    elif project.type_of_project == IDV:
                        type_of_project = 'Identidade Visual'
                    print(f'{project.id} | {project.name} | {type_of_project} | {project.remaining_steps} | {project.manager} | {len(project.consultants)}')
                print('----------------------------\n')
                
                return

        if role == 0:
            match op:
                case '14':
                    print('---------- Avançar Projeto ----------')
                    projects_with_advance_request: list[Projeto] = sys.get_projects_with_advance_requests()
                    if len(projects_with_advance_request) == 0:
                        print('Não há projetos com pedido de avanço')
                        return

                    print('Escolha a ID e sua decisão.')
                    print('ID | Nome do Projeto | Tipo de Projeto | Etapas Restantes | Gerente | # de Consultores\n')
                    for project in projects_with_advance_request:
                        if project.type_of_project == DES:
                            type_of_project = 'Desenvolvimento'
                        elif project.type_of_project == CON:
                            type_of_project = 'Concepção'
                        elif project.type_of_project == IDV:
                            type_of_project = 'Identidade Visual'
                        print(f'{project.id} | {project.name} | {type_of_project} | {project.remaining_steps} | {project.manager} | {len(project.consultants)}')
                    print('----------------------------\n')

                    id = input('ID: ')
                    decision = input('s - Avançar | n - Não avançar: ')
                    if decision == 's':
                        project: Projeto = sys.get_project_by_id(int(id))
                        if project == PROJECT_DOES_NOT_EXIST:
                            print('Esse Projeto não existe.')
                            return
                        project.advance_project(True)
                        print('ID | Nome do Projeto | Tipo de Projeto | Etapas Restantes | Gerente | # de Consultores\n')
                    
                        if project.type_of_project == DES:
                            type_of_project = 'Desenvolvimento'
                        elif project.type_of_project == CON:
                            type_of_project = 'Concepção'
                        elif project.type_of_project == IDV:
                            type_of_project = 'Identidade Visual'
                        print(f'{project.id} | {project.name} | {type_of_project} | {project.remaining_steps} | {project.manager} | {len(project.consultants)}')
                        print('----------------------------\n')
                        print('O projeto foi avançado.')

                    else:
                        project.advance_project_request["Requested"] = False
                        print('O projeto não foi avançado.')

                    print('----------------------------\n')

        elif role == 1:
            match op:
                case '14':
                    print('---------- Avançar Projeto ----------')

                    projects = sys.get_projects_by_username(sys.logged_in_user.username)
                    if len(projects) == 0:
                        print('Não há projetos cadastrados.')
                        print('----------------------------\n')
                        return
                        
                    print('ID | Nome do Projeto | Tipo de Projeto | Etapas Restantes | Gerente | # de Consultores\n')
                    for project in projects:
                        if project.type_of_project == DES:
                            type_of_project = 'Desenvolvimento'
                        elif project.type_of_project == CON:
                            type_of_project = 'Concepção'
                        elif project.type_of_project == IDV:
                            type_of_project = 'Identidade Visual'
                        print(f'{project.id} | {project.name} | {type_of_project} | {project.remaining_steps} | {project.manager} | {len(project.consultants)}')
                    print('----------------------------\n')

                    id = input('ID do projeto que deseja avançar: ')
                    for project in projects:
                        if project.id == int(id):
                            # res = sys.send_advance_project_request(id)

                            if project.advance_project_request["Requested"]:
                                print('Um pedido de avanço ja foi enviado.')
                                print('----------------------------\n')
                                return

                            project.advance_project_request["Requested"] = True
                            project.advance_project_request["RequestedFrom"] = sys.logged_in_user.username

                            print('Sucesso!')
                            print('----------------------------\n')
                            return 
                    
                    print('ID Invalida.')
                    print('----------------------------\n')
                    return
                    


    else:
        match op:
            case _:
                print('Opção Inválida')
                print('----------------------------\n')

##########################

def main():
    # Inicializar o sistema
    sys = Sistema()
    
    role = -1
    while True:
        if isinstance(sys.logged_in_user, Gerente):
            role = 0
        elif isinstance(sys.logged_in_user, Consultor):
            role = 1
        else:
            role = -1

        # Mostrar Opções
        show_options(sys, role)
        op = input('Digite uma opção: ')
        print()

        # Usuario Anônimo
        if not sys.logged_in():
            match op:
                case '': # Limpar console
                    os.system('clear')
                    continue

                case '0': # Sair do Programa
                    return

                case '1': # Login
                    print('---------- Login ----------')
                    username = input('Usuário: ')
                    password = input('Senha: ')
                    res = sys.login(username, password)
                    if res == OK:
                        print('Sucesso!')
                        print('----------------------------\n')
                        continue
                    elif res == WRONG_PASSWORD: 
                        print('Senha errada.')
                        print('----------------------------\n')
                        continue
                    elif res == USER_DOES_NOT_EXIST:
                        print('Usuário não existe.')
                        print('----------------------------\n')
                        continue

                case _:
                    get_options(sys, role, op)

        # Logado 
        elif sys.logged_in():
            match op:
                case '': # Limpar console
                    os.system('clear')
                    continue

                case '0': # Sair do Programa
                    return
                
                case '1': # Logout
                    print('---------- Logout ----------')
                    
                    sys.logged_in_user = None
                    
                    print('Até mais!')
                    print('----------------------------\n')
                    continue

                case _:
                    get_options(sys, role, op)
   
if __name__ == "__main__":
    main()