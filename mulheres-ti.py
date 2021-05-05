import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image



st.sidebar.title("Mulheres na TI")
app_mode = st.sidebar.selectbox("Quer saber mais?",["Introdução","Desafios","Números","Grandes Mulheres na TI"])

if app_mode == "Introdução":
    
    
    st.title("Mulheres na TI")

    image = Image.open('mulheres.png')
    st.image(image, use_column_width=True)

    st.markdown("""As mulheres estão ganhando cada vez mais espaço na cultura e no mercado de trabalho. O direito a voto, ao trabalho
    em tempo integral, ao divórcio, entre muitas outras coisas, foram conquistas que demandaram bastante esforço. E isso se reflete muito
    em nossa sociedade atual, como se observa no caso da presença cada vez maior das mulheres na TI. """)

    st.markdown(""" Muitos não sabem, mas muitas das grandes conquistas que ocorreram no campo da tecnologia são produto do esforço de várias
    mulheres. Mesmo que seus nomes não sejam os mais famosos, muitas de suas criações são altamente influentes até hoje. Claro, isso não significa que os obstáculos foram totalmente eliminados, 
    apenas prova que eles podem ser superados com tempo e esforço.""")
    
    
    st.write("""Lugar de mulher é onde ela quiser, inclusive, na indústria da tecnologia. Seja programando, desenvolvendo produtos
    ou criando inovações, elas sempre estiveram por aí, por mais que nem sempre sejam reconhecidas por seus feitos ou tenham histórias
    que se confundam ou são ofuscadas pelas dos homens. Elas podem até ser pouco lembradas, mas jamais esquecidas. """)
    


elif app_mode == "Desafios":
    st.markdown("**Por quê existem tão poucas mulheres na tecnologia?**")
    st.write("""O principal problema para ingressar as mulheres na TI é uma questão cultural. Ainda é ensinado que tecnologia, matemática, 
    programação não são áreas de estudos para as mulheres. Os cursos de tecnologia cresceram *586%* nos últimos 24 anos aqui no Brasil. 
    No entanto, a participação das mulheres matriculadas apenas diminui com o passar dos tempos. Ela caiu de 34,89% para 15,53%. As mulheres 
    que decidem seguir os estudos na área de tecnologia encontram outros desafios no mercado de trabalho. Elas são desacreditadas por parceiros
    de equipes e clientes, que não acreditam em seu potencial. """)
    
    st.markdown("**Salários menores, poucas oportunidades de crescimento e nichos femininos**")
    st.write(" ")
    image = Image.open('desafios.png')
    st.image(image, use_column_width=True)

    st.write("""Além disso, elas também recebem salários inferiores.A diferença salarial entre os gêneros é um dos primeiros entraves, 
    seguindo uma tendência observada em outros setores. As mulheres ganham 30% menos do que homens na área de TI, de acordo com dados da
    Pesquisa Nacional por Amostra de Domicílios (Pnad), do IBGE, compilados por Bárbara Castro para o seu estudo. """)

    st.write("""A diferença salarial já foi explorada em outras pesquisas, como as da economista americana Linda Babcock, da Universidade Carnegie Mellon, e autora do 
    livro Women Don't Ask (sem tradução para o português). Uma de suas análises aponta que as mulheres ganham menos porque são menos 
    propensas a negociar seus salários depois de uma oferta inicial. Os pesquisadores da equipe de Babcock conduziram o seguinte experimento: 
    diziam aos participantes que eles poderiam ganhar de US$ 3 a US$ 10 para participar de um jogo. Depois do término, o pesquisador ofereceu 
    US$ 3 e perguntou se esse montante estava correto, sem dizer que os participantes poderiam negociar e pedir mais. Se as pessoas pedissem
    mais, ganhariam o que pedissem até o limite de US$ 10. Os homens eram sete vezes mais propensos a pedir mais do que as mulheres. Para 
    descrever a negociação, eles usavam metáforas como “ganhar um jogo”. Já elas, a descreviam como "ir ao dentista".""")


    st.markdown("""Outros estudos exploraram o que acontece quando ambos se comportam de forma assertiva nas negociações salariais. Quando se 
    envolvem exatamente no mesmo comportamento, as mulheres são malvistas por não aceitarem as primeiras ofertas e pedirem mais. “Para nós, 
    de forma geral, negociação significa conflito. Culturalmente, não somos estimuladas a cuidar de nossos interesses, mas a assumir o papel de
    cuidadoras”, diz Dani Botaro, sócia da ImpulsoBeta, uma empresa de inteligência de gênero que apoia corporações a implementarem ações de
    diversidade. """)

    st.markdown("""A organização do mercado brasileiro de tecnologia é outro grande problema. Cerca de 93% dos negócios são de pequeno e médio 
    porte, que comercializam software e hardware para outras empresas. Isso cria uma dinâmica de faturamento por projetos, feitos um em seguida
    do outro ou de maneira concomitante para não perder clientes. O atendimento a diversos clientes faz parte da rotina dos profissionais do 
    setor, com deslocamentos constantes internos e externos às cidades na qual se situa a sede de sua empresa""")

elif app_mode == "Números":
    st.title("Naturalização dos estereótipos")
    st.header("""Dificuldade em matemática""")
    
    image = Image.open('matematica.png')
    st.image(image, use_column_width=True)

    st.markdown("""Pesquisadores das universidades de Nova York, Princeton e Illinois, nos Estados Unidos, investigou o comportamento de crianças
    de 5, 6 e 7 anos em relação a suas habilidades intelectuais. Com 5 anos, elas foram convidadas a ouvir uma história sobre uma pessoa “muito,
    muito inteligente”, sem qualquer pista sobre o gênero do protagonista. Ao serem perguntadas sobre quem seria tal pessoa, escolheram alguém do
    mesmo sexo. A partir dos 6 anos, pelo menos para as meninas, essa identificação começa a diminuir. Os estudos do psicólogo Andrew Meltzoff,
    codiretor do Instituto de Aprendizado e Ciências do Cérebro da Universidade de Washington, apresentam mais evidências sobre o poder dos estereótipos
    culturais no aprendizado das crianças. A pesquisa aponta dados parecidos: “Muito cedo, as garotas incorporam falsas concepções de que não 
    são boas em Matemática”, escreve os autores no artigo Estereótipos de Gênero e Matemática em Crianças da Escola Primária.""")

    st.header("""Leitura por diversão""")
    
    image = Image.open('leitura.png')
    st.image(image, use_column_width=True)

    st.markdown("""Essa lógica atravessa toda a trajetória educacional das garotas, com desdobramentos em suas escolhas futuras, incluindo a 
    profissão. Ao fim da educação básica, uma parcela ínfima delas deseja estudar tecnologia e áreas correlatas, como mostram as matrículas das 
    principais universidades do país. Na Unicamp, por exemplo, só 12,3% dos aprovados no vestibular de Ciências da Computação em 2016 eram 
    mulheres. "Você tem certeza que quer estudar nessa faculdade? Não sabemos se você consegue", ouviu Lucía Salamanca, 27 anos, de parentes.
    O pai de Larissa Pereira Gambale foi mais direto. “Quando passei na faculdade de análise de sistemas, ele não queria que eu seguisse essa 
    área. ‘Você não vai trabalhar no meio de homens. Faça administração’.”""")

    st.header("""Carreira em tecnologia""")
    
    image = Image.open('carreira.png')
    st.image(image, use_column_width=True)

    st.markdown("""Metade dos pais no Chile, Hungria e Portugal esperam que seus filhos sigam uma carreira nas áreas tecnológicas, enquanto 
    só 20% veem as filhas fazendo o mesmo.” Chama atenção, porém, que a preferência feminina ainda recaia sobre as áreas de humanas e saúde.
    Enfermagem, por exemplo, tem 84,4% de alunas. Historicamente, as matrículas das mulheres no ensino superior estiveram concentradas em 
    determinadas áreas, como ciências humanas, letras e artes, reforçando a divisão sexual do trabalho. Já entre o público masculino, os dados
    mostram que as áreas de maior inserção estão ligadas às exatas, como as engenharias e cursos relacionados à tecnologia, como ciências da
    computação, que chega a ter 85,4% de homens.""")

    st.header("""Matrículas no Ensino Superior""")
    
    image = Image.open('superior.png')
    st.image(image, use_column_width=True)

    st.markdown("""A inclusão das garotas nas profissões científicas tem-se dado em ritmo mais lento do que em outras áreas e há uma tendência
    de as ciências exatas – matemática, física, engenharias– atraírem relativamente poucas mulheres. Nos últimos anos, as brasileiras perderam
    representatividade nos cursos relacionados à computação. Em 2013, passaram a representar apenas 15,53% dos ingressantes, segundo o Censo
    da Educação Superior.”""")

    st.markdown("""Na maioria das vezes, o ambiente universitário mostra-se pouco acolhedor, o que explica o aparente desinteresse e as altas
    taxas de evasão. “Antiquado e cruel”, na definição da programadora Camilla Falconi, 29 anos. A maioria dos colegas dela já tinha feito 
    curso técnico, conhecia webdesign ou tinha tido acesso a códigos ou exercícios de lógica previamente. “Sem a mesma experiência quando 
    entra no curso, você se sente incapaz, e muitas vezes quer desistir”, diz ela. Uma parcela significativa desiste de fato: 79% as mulheres
    que ingressam em formações relacionadas à área de TI abandonam a faculdade ainda no primeiro ano, segundo dados da Pnad. "Uma vez, fiz
    uma pergunta ao professor sobre algoritmos. Um menino disse que, se estivesse tão difícil pra mim, que eu fosse fazer balé", diz Lidiane
    de Paula, 30 anos, que estudou sistemas de informação. "Um professor ridicularizou uma colega de classe perguntando se ela era casada.
    Disse que ela deveria casar logo, pois quem continua solteira não é bem vista pela sociedade. Confrontei o professor, em uma sala em
    que 95% dos alunos eram homens, e disse que ter ou não ter um namorado ou marido não muda em nada nosso sucesso ou objetivos de vida.
     Depois, ele tentou confirmar o que tinha dito antes, tirando sarro do que eu havia acabado de dizer", conta Mariana Carvalho, 24.”""")

    st.header("""Futura carreira""")
    
    image = Image.open('futuro.png')
    st.image(image, use_column_width=True)

    st.markdown("""Quatro vezes mais meninos planejam seguir uma carreira profissional em engenharia ou informática.Também são comuns os casos
    de estudantes que são ignoradas pelos professores e colegas. “Já passei por situações em que professores (homens) me ignoraram em relação a 
    dúvidas e deias que eu tinha sobre as matérias, mas para meus colegas eles estavam sempre disponíveis”, diz Sara Maria Gonçalves, 20 anos,
    que estuda Sistemas de Informação. “Era menosprezada na sala de aula por gostar de me arrumar, passar batom, pintar as unhas. Já tive que
    ouvir que não precisava me arrumar tanto para ir a faculdade, que estava perdida e não sabia o que queria da vida e que fazia o curso só
    para passar o tempo”, diz Heloisa Frasão, 24 anos. Ela é uma das seis meninas de uma sala com aproximadamente 40 alunos. Já Juliana Neres,
    21 anos, tinha interesse em se inscrever numa competição com um grupo de amigas. “Escutei de um colega do curso de análise e desenvolvimento
    de sistemas: ‘Vocês querem competir com um time de meninas ou com um time que vai ganhar?’”. “Um professor disse que ‘mulher não devia 
    fazer computação’ e reprovou todas as alunas da turma”, diz Clarissa Xavier, 40 anos.”""")

elif app_mode == "Grandes Mulheres na TI":
    st.title("Grandes Mulheres da TI")
    st.write("""Algumas pessoas ainda duvidam da relevância feminina no desenvolvimento da Tecnologia da Informação, o que é certamente um grande 
    erro. Vejamos alguns dos nomes que provam isso.""")

    st.header("""Ada Lovelace""")
    
    image = Image.open('ada.png')
    st.image(image, use_column_width=True)

    st.markdown("""Em 1843, Augusta Ada King, a Condessa de Lovelace, traduzia os textos de Luigi Menabrea, um matemático italiano, sobre as
    ferramentas analíticas usadas por Charles Babbage, um matemático inglês. Esse trabalho derivativo resultou no que, para muitos especialistas,
    é o primeiro algoritmo criado na história, muito antes da existência de máquinas que pudessem processá-lo. Única filha legítima de Anne
    Isabella Milbanke e do poeta Lord Byron, ela foi uma das precursoras das ciências da computação. Seu trabalho estava relacionado à 
    metodologia de cálculo de uma sequência de números de Bernoulli, sequências de racionais com operações altamente complexas.”""")

    st.markdown("""O único problema encontrado por Lovelace, na época, é que ela simplesmente não possuía o maquinário necessário para
    colocar seus estudos à prova. Seu algoritmo, entretanto, foi provado como correto anos depois de seu falecimento, quando finalmente 
    chegaram os equipamentos necessários para essa verificação. Hoje, ela dá nome a um prêmio da Sociedade Britânica de Computação que 
    contempla avanços significativos em sistemas de informação.”""")

    st.header("""Jean Sammet""")
    
    image = Image.open('jean.png')
    st.image(image, use_column_width=True)

    st.markdown("""Erroneamente chamada de primeira mulher a obter um PhD em ciências da computação – ela obteve o diploma apenas em 1968,
    três anos depois da Irmã Keller –, Sammet foi a criadora de uma das primeiras linguagens computadorizadas existentes. O FORMAC,
    que entrou em uso no final dos anos 1960 pelas mãos da IBM, era utilizado para manipular fórmulas matemáticas e auxiliar em cálculos
    complexos.”""")

    st.markdown("""Nada mais justo vindo das mãos de uma mulher que, antes de se tornar doutora em ciências da computação, trazia consigo
    duas formações distintas em matemática, uma pela Universidade de Illinois e outra pelo Mount Holyoke College. Por causa disso e de 
    seus conhecimentos em informática, ela trabalhou durante 27 anos na IBM, que por muito tempo foi a empresa símbolo dessa indústria 
    em todo o mundo.”""")

    st.markdown("""Ela também teve influência importante na criação do COBOL e participou de diversas entidades voltadas à inclusão das
    mulheres na indústria da tecnologia. Sammet também presidiu a ACM (Associação para Maquinaria de Computação, na tradução do inglês),
    uma iniciativa voltada para o uso da informática em projetos científicos e educacionais, com mais de 70 mil membros.”""")

    st.header("""Grace Hopper""")
    
    image = Image.open('grace.png')
    st.image(image, use_column_width=True)

    st.markdown("""Quando se fala em pioneirismo, Grace Hopper tem diversos títulos para chamar de seus. Ela foi a primeira mulher a se formar 
    na prestigiosa Universidade de Yale, nos Estados Unidos, com um PhD em matemática, além de ter sido a primeira almirante da marinha dos EUA.
    No campo da tecnologia, ela foi uma das criadoras do COBOL, uma linguagem de programação para bancos de dados comerciais.”""")

    st.markdown("""Entretanto, sua história mais famosa é a que remonta à popularização do termo “bug” para indicar problemas em software. Em 
    uma anedota jamais confirmada, ela teria resolvido um problema de processamento de dados ao remover uma mariposa que estava criando ninho
    dentro de um computador, indicando que um “debugging”, ou a remoção de um “inseto” é o melhor caminho para resolver falhas de funcionamento.”""")

    st.markdown("""Uma de suas principais frases se tornou não apenas um bastião feminista, mas também o principal mote para as mulheres que 
    lutam por representatividade na indústria da tecnologia: “é mais fácil pedir perdão do que permissão”. Além do COBOL, Hopper também criou
    linguagens de programação para o UNIVAC, o primeiro computador comercial fabricado nos Estados Unidos.”""")

    st.header("""Carol Shaw""")
    
    image = Image.open('carol.png')
    st.image(image, use_column_width=True)

    st.markdown("""Citada como a primeira mulher a trabalhar na indústria dos games, Carol Shaw foi uma das funcionárias originais da Atari.
    Apesar disso, ela passou pouco tempo na empresa, sendo contratada rapidamente pela Activision e participando do desenvolvimento de um dos 
    maiores clássicos dos games, River Raid.”""")

    st.markdown("""Seu cartão de visitas a atribuía a função de “engenheira de software para microprocessadores”, o que significava que ela 
    atuava também nos sistemas do próprio console. E trabalhando com uma máquina com apenas 128 bytes de memória RAM, ela foi a responsável por
    criar o primeiro sistema de geração procedural de conteúdo, o que significava que, em River Raid, uma fase nunca era igual à outra. 
    Oponentes, itens e objetos do cenário apareciam de forma randômica, em uma prática que é utilizada até hoje.”""")

    st.markdown("""Em seu currículo, também estão games clássicos como 3D Tic Tac Toe, Super Breakout e Happy Trails, seu últmo game com a 
    Activision. Ela se aposentou em 1990 e mora na Califórnia, nos Estados Unidos, onde realiza trabalho voluntário.”""")

    st.header("""Radia Perlman""")
    
    image = Image.open('radia.png')
    st.image(image, use_column_width=True)

    st.markdown("""Se Tim Berners-Lee é o pai da internet, Radia Perlman pode ser considerada como a mãe. Designer de software e engenheira
    de redes, ela foi a responsável pela criação do protocolo STP (Spanning Tree Protocol), que melhorou a performance de sistemas conectados
    ao evitar a realização de loops de dados, garantindo que as informações trafeguem mesmo em caso de problemas, sem ficarem perdidas tentando
    firmar uma conexão inexistente.”""")

    st.markdown("""Imagine que você precise chegar ao outro lado de um rio e possui diversas alternativas para fazer isso – uma ponte de madeira
    frágil, uma com elevações, outra que desce até a água para depois subir e, finalmente, aquela em linha reta, a mais eficiente, feita de 
    concreto. O protocolo de Perlman permite que os dados, como você, saibam que aquele é o caminho mais rápido para chegar ao destino. Caso algo
    dê errado, ele também permite mensurar qual é o segundo melhor, e assim por diante.”""")

    st.markdown("""Ela também é uma das pioneiras no ensino de programação e arquiteturas de redes para crianças, além de ter sido uma das criadoras
    do TORTIS, uma linguagem de programação com fins também educacionais, só que de robótica. Ela também foi a responsável por diversos protocolos
    de segurança de rede e, hoje, trabalha na Intel, além de ser dona de mais de 50 patentes relacionadas a tecnologias de conexão.”""")



