# ETL_Airflow
Agendando um job para ETL no Airflow,nosso codigo gera um token de acesso, usa para chamar a API e grava os dados de acesso no banco. Esse processo todo é feito em uma DAG com dois passos. 

Essa é a Graph View do nosso codigo:

   ![image](https://github.com/gabrielabrag/ETL_Airflow/assets/108342265/f4817fa8-ab6c-479c-abc1-c0bf27187f9b)

O Apache Airflow é uma ferramenta de código aberto(open-source) que pode ser usada para automatizar os fluxos de trabalho em ETL(Extração, Transformação e Carga de Dados) no setor de ciência de dados. Ele permite criar, monitorar e gerenciar processos de ETL em um sistema centralizado

Algumas das vantagens em utilizar o Airflow:

•	Flexibilidade: O Airflow é altamente flexível e pode se integrar a uma variedade de sistemas de backend e ferramentas de processamento de dados; 

•	Programação em Python: Como os fluxos de trabalho são programados em Python, os Engenheiros de Dados podem usar todas as vantagens da linguagem, como facilidade de uso, capacidade de criação de scripts complexos e automação de tarefas no sistema operacional como movimentação de arquivos, por exemplo;

•	Escalabilidade: O Apache Airflow é escalável e pode lidar com um grande volume de fluxos de trabalho e tarefas;

•	Monitoramento e Notificação: A interface do usuário permite o monitoramento em tempo real dos fluxos de trabalho e o envio de notificações em caso de falhas;

  
O Apache Airflow é gratuito e permite que empresas e profissionais testem e usem a ferramenta em diferentes cenários e projetos de Engenharia ou Arquitetura de Dados sem custo de licença de software. 
