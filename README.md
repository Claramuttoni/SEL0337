# SEL0337

# Prática 1
- Foi executada a seguinte atualização no terminal Linux da Raspberry Pi:
    sudo rpi-updatecac01bed1224743104cb2a4103605f269f207b1a #6.1.54

- Criou-se um diretório de trabalho onde escreveu-se um programa chamado blink.sh para realizar o blink de um LED conectado à GPIO da Rasp.
    #!/bin/bash
    echo 18 > /sys/class/gpio/export
    echo out > /sys/class/gpio/gpio18/direction
    while [ 1 ]
    do
      echo 1 > /sys/class/gpio/gpio18/value
      sleep 0.2s
      echo 0 > /sys/class/gpio/gpio18/value
      sleep 0.2s
    done

- Por fim, utilizou-se o comando "chmod +x blink.sh" e "./blink.sh" para executar o programa
- Além disso, criou-se também o arquivo chamado “blink.service”, com o conteúdo:
    [Unit]
    Description= Blink LED
    After=multi-user.target
    [Service]
    ExecStart=/home/sel/blink.sh
    #ExecStop=
    user=SEL
    [Install]
    WantedBy=multi-user.target

- Em seguida, os seguintes comandos foram executados:
    sudo cp blink.service /lib/systemd/system/
    sudo systemctl start blink
    sudo systemctl stop blink
    sudo systemctl enable blink


# Prática 2

- Para a prática 2, foi criada essa conta no GitHub e um repositório com código da disciplina para documentar o projeto dentro dele a partir da Raspberry Pi, realizando um clone do repositório na Raspberry Pi para inserir os programas em python desenvolvidos e realizar commits, push para enviar as atualizações que realizar localmente para o repositório remoto na nessa conta do GitHub.
- Assim, foi possível também configurar o acesso da dupla por meio dos comandos "git config --global user.name "claramuttoni" e "git config --global user.email "claramuttoni@usp.br"

A seguir, está uma imagem dos processos realizados na prática 2:
![WhatsApp Image 2024-11-24 at 23 34 57](https://github.com/user-attachments/assets/c112ca08-e03e-448d-a55f-110a884dcdfa)
