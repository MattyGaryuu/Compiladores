class glc:

    '''glc é o módulo que contém a definição e principais funções para gramáticas livres de contexto'''

    def __init__(self):

        ''' toda gramática tem:
            1. um conjunto de não terminais
            2. um conjunto de terminais
            3. um símbolo inicial
            4. um conjunto de produções'''

        self.Vn = []    # conjunto de não terminais
        self.Vt = []    # conjunto de terminais
        self.S = None   # símbolo terminal
        self.P = {}     # conjunto de produções A -> abc = {'A':'abc'} (dicionário)
        self.F = []     # conjunto de sentenças criadas pela gramatica livre de contexto
        self.Fs = []    # Sentenças geradas

    def insereNaoTerminal(self, A):

        '''glc.insereNãoTerminal(A) insere um não terminal no conjunto de não terminais da gramática'''

        self.Vn.append(A)

    def insereTerminal(self, a):

        '''glc.insereTerminal(a) insere um terminal no conjunto de terminais da gramática'''

        self.Vt.append(a)
        
    def defineSimboloInicial(self, S):

        '''glc.defineSimboloInicial(S) define um não terminal como símblo inicial da gramática'''

        self.S = S

    def insereProducao(self, p):

        '''glc.insereProducao(p) insere ums produção no conjunto de produções da gramática'''

        self.P.update(p)

    def mostraGramatica(self):

        '''glc.mostraGramatica() mostra cada um dos elementos da gramática'''

        print(f'Não Terminais: {self.Vn}')
        print(f'Terminais: {self.Vt}')
        print(f'Símbolo Inicial: {self.S}')
        print(f'Produções: {self.P}')
        print(f'Sentenças Geradas: {self.Fs}')

    def gerarNSentencas(self,nt, N, sen, first): #nt = Não terminal atual, N = quantidade de numeros, sen = sentença atual, first= Verificar se é a primeira vez que o codigo é chamado

        '''glc.gerarNSentencas mostra cada setença que pode ser gerada com até N numeros'''

        CF = False
        if not first:
            for j in range(0,len(sen)): #For para verificar se a sentença tem um não terminal, se não possuir retornará
                for z in range(len(self.Vn)):
                    if sen[j] == self.Vn[z]:
                        CF = True
            
            if not CF:
                self.Fs.append(sen)
                return
        if first:
            pen = self.P.get(nt) #Resgatar produções do Não Terminal
            Tam = len(pen) #tamanho do nao terminal
            for i in range(0,Tam):
                CF = False
                sen = str(pen[i])
                for j in range(0,len(sen)):
                    for d in range(len(self.Vn)):
                        if sen[j] == self.Vn[d]:
                            self.gerarNSentencas(self.Vn[d],N,sen,False)
                            CF = True
                if not CF:
                    self.Fs.append(sen)
            self.Fs = list(set(self.Fs)) #deletar sentenças já existentes
            self.Fs.sort(key=len) #organizar
            return

        pen = self.P.get(nt) #Resgatar produções do Não Terminal
        Tam = len(pen) #tamanho do nao terminal
        for i in range(0,Tam): #para cada Produção do não terminal
            for j in range(0,len(sen)): #verifica se na sentença
                CF = False
                for z in range(len(self.Vn)): #há determinado Nao terminal
                    if sen[j] == self.Vn[z]: #se possuir
                        penT = self.P.get(self.Vn[z]) #resgatar sentenças
                        for y in range(0,len(penT)):
                            CF = True
                            sen1 = sen.replace(str(self.Vn[z]),str(penT[y]))
                            #verificar se é uma sentença completa
                            if len(sen1) <= N:
                                self.gerarNSentencas(self.Vn[z],N,sen1,False)
                        return