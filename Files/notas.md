## Reading and writing
fout = open('output.txt', 'w') se output.txt já existe, sera sobrescrito, se não existe, será criado, podemos adicionar dados ao arquivo através do método .write() que recebe uma string;  
quando terminar-mos de manipular o arquivo precisamos fechá-lo com .close();  
## Format Operator
% é o format operator, apenas quando o primeiro operando é uma string, aplicado a ints ele é o modulus operator;  
o primeiro operando é a format string, que contem uma ou mais sequencias formataveis, que especificam como o segundo operando é formatado, o resultado é uma string;  
camels = 42  
'%d' % camels  
'42'  
d significa decimal, %d é uma sequencia formatável que remete a algum valor que será passado após o format operator, mas precisa ser do tipo correto;  
se há mais de uma sequencia formatável na string, o segundo operando precisa ser uma tupla, na ordem em que a format sequence aparece na string;  
'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')  
'In 3 years I have spotted 0.1 camels.'  
## Filenames e Paths
Arquivos são organizados em diretórios, todo programa executando tem um 'diretório atual' 'current directory' que é o diretório padrão para a maioria das operações do programa, quando um programa abre um arquivo para leituro o Python procura por ele no 'diretório atual';  
o módulo 'os' fornece funções para trabalhar com arquivos e diretórios ('os' significa operating system);  
os.getcwd() retorna o nome do 'current working directory';  
cwd = os.getcwd();  
uma string que identifica um arquivo (com seu caminho de diretórios) é chamada path (caminho), um path relativo começa do diretório atual, um path absoluto começa do diretório mais alto do sistema de arquivos;  
os.path.abspath() (retorna o caminho absoluto);  
os.path.exists() (checa se um arquivo ou diretório existe);  
os.path.isdir() (checa se é um diretório), os.path.isfile() (checa se é arquivo);  
os.listdir(cwd) (retorna uma lista de arquivos e diretórios de um dado diretório);  
### Exercicio 14.1
walk.py
## Pegando Exceções
IOError Errno 2 No such file or directory;  
IOError Errno 13 Permission denied;  
IOError Errno 21 Is a directory;  
Poderiamos tentar evitar todos os erros possíveis para abertura de arquivos, mas isso daria muito, muito trabalho;  
Ao invés disso podemos usar a instrução Try para tentar e depois lidar com os erros se eles acontecerem;  
uma forma de pegar uma exceção é através do par Try Except, dentro do bloco Try dizemos o que o programa deve tentar fazer, e no bloco except podemos passar uma mensagem de erro no caso do bloco Try não dar certo;  
usar a instrução try para lidar com uma exceção é chamado de catch an exception, em geral pegar uma exceção nos da a chance de consertar o problema, ou tentar novamente ou pelo menos terminar o programa graciosamente;  
### Exercício 14.2
Escreva uma função chamada sed que recebe como argumentos uma string padrão, uma string de substituição, e dois nomes de arquivos, a função deve ler o primeiro arquivo e escrever no segundo arquivo, se a string padrão aparece no arquivo ela deve substituir com a string de substituição, esse programa deve pegar a exceção, imprimir uma mensagem de erro e sair;  
sed.py;  
## Databases
database é um arquivo organizado para estocar dados, a maioria das databases estão organizadas como um dicionário no sentido que elas mapeiam de chaves para valores, a principal diferença é que a database está no disco (ou algum outro método de estocagem permanente) então a database persiste depois que o programa termina;  
O módulo 'dbm' fornece uma interface para criar e atualizar arquivos de base de dados;  
uma limitação para esse módulo que tanto chaves quanto valores precisam ser strings, o módulo 'pickle' pode ajudar, ele traduz quase qualquer tipo de objeto para string disponível para estocagem em base de dados, e depois traduz novamente para objetos, pickle é um serializador desserializador;  
pickle.dumps pega um objeto e retorna uma representação string;  
pickle.loads recontroi o objeto a partir de uma string criada com pickle.dumps();  



