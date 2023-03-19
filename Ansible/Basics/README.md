# Ansible Basics
These study notes were obtained based on the information obtained from:
- watching the [ANSIBLE BASICS: AUTOMATION TECHNICAL OVERVIEW (DO007)](https://rhtapps.redhat.com/promo/course/do007), understanding it and typing out a summed up version of it.
- researching any doubt in the [Official Ansible Documentation](https://docs.ansible.com). Images were extracted from the official domentation too.
## Products
###  RedHat Ansible Automation Platform (paid)
Paid platform that contains several products:
- **Ansible Automation Controller**:
    Evolution of Ansible Automation Tower. **Has an open source free upstream version called AWX**
    - Characteristics of Ansible Automation Controller:
        1. Is a UI and RESTful API tool.
        2. Has RBAC.
        3. Has centrally logged controller app.
        4. Used for deployments.
    - Based on:
        - **Projects**: Logical collection of Ansible Playbooks. Can use Git, Subversion... as the source of the project.
        - **Jobs / Job Templates**: Will be executed against a playbook, using credentials. All inside a project. 
        - **Workflow templates**: Proccess of running multiple jobs in serial/parallel based on condition from previous jobs and so on. This would replace conditions to run certain tasks in playbooks.
            -  Has a Workflow visualizer: 
                
                ![Workflow visualizer example](https://docs.ansible.com/ansible-tower/latest/html/userguide/_images/wf-node-all-scenarios-wf-in-wf.png)
                - It is a visual way to see a workflow template.
                - Lines describe the proccess of the workflow: 
                    - Blue lines always run. > Backup config job
                    - Green lines run if previous job template was successful. > Two job templates: Configure a new user, and also configure static ip address
                    - Red lines will only run if one of the previous job templates fail. > Restore backed up config job and alert via mail that x host was not configured correctly job.
        - **Surveys**: A fancy easy way to launch jobs/workflow templates based on custom questions/answers.
            - Why? > The idea is to allow to launch certain jobs/workflow templates to be run from people that needs periodical things and that do not need to know everything regarding Ansible: restart x server/proccess on certain servers, obtain y information from x server, etc.
            - How to create a Survey? > You first need to have a job/workflow template, then you go to Survey inside the job and add one new survey.
        - **Schedules**: Allows to run a job every hour/day/week/month... (cron)
        - **Credentials**: It can be static (git, subversion repo...) or dynamic(CyberArk or any other "privileged credentials manager"): 
            - Contains hostname/ip + username + ssh_key/password, organization (Groups that are named for better management of hosts)... of hosts in inventory. Also can contain Redhat.io credentials for Execution Environments, Azure Credentials, etc. etc.
        - **Inventory**: Playbooks are executed on inventories, which contains groups of hosts, with specific variables, from static or dynamic sources (AWSs active EC2 for example, GCP, Azure...).
        - **Role-Based Access Control (RBAC)**:
            - User Management Components:
                - Organization: High level collection of users.
                - Teams: Sub division from organizations.
                - User: Member from the organization.
            - You can add the privilege to run, execute, read a project for example to a certain user/team, also to see x elements from the y inventory, hosts, credentials...
            - User type: (User, admin...)
            - Access to specific credentials can be given to particular users.

- **Automation Mesh**

- **Automation Execution Environments**: 
    
    Collections + Dependancies Libraries + ansible core (all in one, so no need to install specific versions)

### Free products:
- **`ansible / ansible-playbook / ansible-navigator`**: 
    
    Main CLI tools. Allow to run playbooks, to check all facts, etc. Ansible playbook was replaced by Ansible navigator.
- **`ansible-navigator`**: 

    Free CLI tool to navegate over the executions in a much more visual and practical way.
- **AWX**: 
    
    Used to be an open source ansible tower upstream, now it is an automation controller upstream.
- **Ansible repositories**:

    **`ansible-galaxy`**: Command that works for both, ansible galaxy main repo and private automation hub.
    - **Ansible galaxy**: 
    
        The main repository for public content for Ansible. Anybody can upload content. 
    - **Private Automation Hub**: 

        Private-repositories of Ansible content.

## Ansible "actors":
- **Playbook**. Contains:
    - play: What is going to be done, on which hosts and with whatever plugins that are needed. 
    - modules/tasks: To do things
    - roles: full playbooks with multiple modules to be applied. Can be added to a playbook.
- **Inventory**: Playbooks are executed on inventories, which contains groups of hosts, with specific variables, from static or dynamic sources (AWSs active EC2 for example, GCP, Azure...).

Tip: It is ideal to avoid using inventories in the playbook itself when we start reusing playbooks over and over as jobs via Ansible AWX/Tower/Automation Platform. Because without using this tip, the playbooks will be useless outside an specific inventory.
- **Credentials**:
    - Contains hostname/ip + username + ssh_key/password... of hosts in inventory. Also can contain Redhat.io credentials for Execution Environments, Azure Credentials, etc. etc.
    - Can be gathered from CyberArk, a security vault of privileged accounts with password management, session recording, etc., etc., 
    - Can be manually added to Ansible Vault(ansible-vault), a secrets manager...

- **Collections**:
    The way of sharing Ansible content. (file structure): Includes:
    - modules
    - playbooks
    - roles
    - plugins
    - docs
    - tests
- **Ansible servers**:
    - ansible control node: linux server that runs the code on remove over the managed nodes.
    - managed nodes: nodes that are controlled by the ansible control node.
- **Ansible commands**:
    - "check" Command-line option checks the status of the playbook, without modifying anything on the node. Without the check option the playbook will be launched.

        **`ansible-playbook foo.yml --check --mode stdout`**
    - Check all facts (variables):
        
        **`ansible -m setup localhost`**
    - Execute a playbook with a nice graphical interface:

        **`ansible-navigator run main.yml`**
    - Executes a playbook with stdout mode:

        **`ansible-navigator run main.yml --mode stdout`**

    Note: Executing a playbook will make some artifact .json files with datetime, so everyone can check output from the playbook execution.
## Dive on ansible playbooks:
Remember: You can always search in the official documentation for help in any module, like [apt](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_module.html)
- Facts (variables):
    ```
    ---
    - name: Output facts # Descriptive name of the play.
    hosts: all # Hosts that will get the Ansible tasks applied to. 
    gather_facts: true # Gather facts from the hosts.
    tasks:
        -name: Print Ansible facts # Descriptive name of the task.
            debug: # debug: msg: will show a message in the console.
            msg: The default IPv4 of ({{ ansible_fqdn }}) is ({{ ansible_default_ipv4.address }}). Check others facts with ansible -m setup localhost

    #host vars overrides groups vars.
    ```
- Status handling (Conditionals: When & Register):
    - when (Works just like an if):
        ```
        tasks:
            - name: Install apache on Debian/Ubuntu
                apt: 
                    name: apache2 # Will install apache2/check if already installed via apt
                    state: latest # Ensure that latest version is the version to install
                when: ansible_distribution == 'Debian' or ansible_distribution == 'Ubuntu' # If the host is Debian or Ubuntu will run the task, otherwise, will do nothing.
            - name: Install httpd on CentOs
                yum: 
                    name: httpd # Will install httpd/check if already installed via yum
                    state: latest
                when: ansible_distribution == 'CentOs'
        ```
    - register (Saves event status to use the status in future "when"(s)):
        ```
        tasks:
            - name: Ensure httpd package is present
                yum:
                    name: httpd
                    state: latest
                register: httpd_results #Save event status from this task (whether httpd has been installed), then does the task below that has a when: httpd_results.changed
                
            - name: Restart httpd
                service: httpd
                state: restart
                when: httpd_results.changed
        ```
- Status handling (Conditionals: Notify & Handlers), notify & handlers: 

    This is the best way of running operations on change in Ansible , just in case we need to call the same tasks with "multiple "when"" functionality:
    ```
    - name: Ensure httpd package is present
    yum:
        name: httpd
        state: latest
    notify: restart_httpd # After executing the task will notify the restart_httpd handler
        
    handlers:
    - name: restart_httpd
        service:
            name: httpd
        state: restart # Will restart httpd.
    ```
- loops:
    ```
    ---
    - name: Ensuring users are there
    hosts: localhost
    
    vars:
        user1: paco
        user2: paca
        user3: itamar

    tasks:
        - name: Ensure user {{ user1 }} is present
            user:
                name: {{ user1 }}
            state: present

        - name: Ensure user {{ user2 }} is present
            user:
                name: {{ user2 }}
            state: present
            
        - name: Ensure user itamar is present
            user:
                name: itamar
            state: present
    ```

    It is better to use lists if the module allows so, for example, yum does allow it.

    The above yaml can be replaced with:
    ```
    ---
    - name: Ensuring users are there
    hosts: localhost
    
    vars:
        user1: paco
        user2: paca
        user3: itamar
        
    tasks:
        - name: Ensure user {{ user1 }} is present
            user:
            name: ``{{item}}´´
            state: present
            loop:
            - {{ user1 }}
            - {{ user2 }}
            - itamar
    ```

## Dive on Ansible playbooks: Template
- Creating a web server:

    Here you can see how to copy files from control node to destiny, 
    1. httpd.conf:
        ```
        ---
        - name: Ensure apache is installed and started.
        hosts: web # Execute the playbook  on host group "web".
        become: yes # Execute the commands as root.
        
        vars:
            http_port: 80 # Configures the web server port.
            http_docroot: /var/www/mysite.com # Decides the folder that will have the web server.
            
        tasks:
            - name: Verify correct config file is present
                template:
                    src: templates/httpd.conf.j2 # Jinja2 configuration file that will be copied from the control node
                    dest: /etc/httpd/conf/httpd.conf # Destination inside the web servers.
        ```

    2. templates/httpd.conf.j2:
        ```
        Listen {{ http_port }}
        DocumentRoot {{ http_docroot }}
        ```

    3. motd:
        ```
        ---
        - name: Fill motd file with host facts
        hosts: node1
            become: true
            tasks:
            - template:
                src: motd-facts.j2
                dest: /etc/motd
                owner: root # Sets the user owner of the file
                group: root # Sets the group owner of the file
                mode: 0644 # File permissions of rw-r--r--
        ```

    4. motd-facts.j2:
        ```
        Welcome to {{ ansible_hostname }}.
        {{ ansible_distribution }} {{ ansible_distributio_version }}
        deployed on {{ ansible_architecture }} architecture,
        running kernel on {{ ansible_kernel }}.
        ```    

- A collection folder example + how to use roles:
### Directory layout:
For better content sharing cappabilities, it is recommended to use a common directory layout available in [the Best Practices from Ansible](https://docs.ansible.com/ansible/2.8/user_guide/playbooks_best_practices.html#directory-layout).
> 0.0-support-docs
>
> 1.1-setup
>
> 1.2-adhoc
>
> 1.3-playbook
>
> 1.4-variables
>
> 1.5-handlers
>
> 1.6-templates
>
> 1.7-role
>
> - roles
>
>   - apache_vhost
>
>       - vars (variables that override defaults and have the tendancy of being modified more often than defaults)
>
>           - main.yml
>
>       - defaults (variables that are overrided)
>
>            - main.yml
>
>       - files (holds files that we will need, like the web index)
>
>            - web.html
>
>       - templates #(holds template txt config files)
>
>            - vhost.conf.j2
>
>       - meta (holds role metadata (including dependencies))
>
>            - main.yml
>
>       - handlers #(handlers)
>
>            - main.yml
>
>       - tasks #(main file of the of the playbook)
>
>            - main.yml
>
>       - tests #(playbook tests)
>
>            - inventory
>
>            - test.yml
>
>       - README.md
>
>   - test_apache_role.yml

### Files: 
- 1.7-role/test_apache_role.yml:
    ```
    ---
    - name: use apache_vhost role playbook
        hosts: node2
        become: true

        pre_tasks:
            - debug:
                    msg:'Beginning web server configuration'
                    
        roles:
            - apache_vhost #Tasks main.yml file will be executed. #imagine "itamar.itamar_collection.apache_vhost" instead. We would use the role apache_vhost inside the globally available collection itamar.
            
        post_tasks:
            - debug:
                    msg: 'Web server has been configured'
    ```

- 1.7-role/roles/apache_vhost/tasks/main.yml:
    ```
    ---
    - name: install httpd
        yum:
            name: httpd
            state: latest

    - name: start and enable httpd service
        service:
            name: httpd
            state: started
            enabled: true
            
    - name: ensure vhost directory is present
        file:
            path: "/var/www/vhosts/{{ ansible_hostname }}"
            state: directory

    - name: deliver html content
    copy:
            src: web.html
            dest: "/var/www/vhosts/{{ ansible_hostname }}/index.html"
            
    - name: template vhost file
        template:
            src: vhost.conf.j2
            dest: /etc/httpd/conf.d/vhost.conf
            owner: root
            group: root
            mode: 06444
        notify:
            - restart_httpd
    ```

- 1.7-role/roles/apache_vhost/handlers/main.yml:
    ```
    ---
    - name: restart_httpd
        service:
            name: httpd
            state: restarted
    ```