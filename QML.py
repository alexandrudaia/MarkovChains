
class  qml(object):
    def __init__(self,data):
        self.data=data
    def  get_chunck(self,index,chain_order):
        data=self.data
        if index+1-chain_order<0:
            print("chain order must   smaller  then   sequence length")
        else:
            chunck=[]
            start=index+1-chain_order
            end=index+1
        return(data[start:end])
    def  MLH(self,index,chain_order):
        #makes   probabilty  estimate according  to  degree  of   markov chain order  with the   natural maximum 
        #likelihood estimator  like this( could be generalized)
        #Q(ement/first_previous_element,second_previous_element)=
        #card({elem,first_previous_element,second_previous_element})/card({previous_element,second_previous_element})
        #form entity  history
        chunk=self.get_chunck(index,chain_order)
        nominator=chunk
        denominator=chunk[:-1]
        data=self.data
        card_nominator=sum(data[i:i+len(nominator)]==nominator for i in range(len(data)))
        card_denominator=sum(data[i:i+len(denominator)]==denominator for i in range(len(data)))
        q=card_nominator/card_denominator
        #q is the modeled probability   of    occuring   value   at inde conditioned  my   markov chain  order
        return(q)
    def  interpolation(self,lambda_list,chain_order_list):
        """lambda  list  of lambdas like  lambda1 , ....,lambdak,  chain_order_list=[index,chain_order]"""
        print("TO DO  BEYHAN")
        print("TO   FIGURE OUT  EMPIRICAL  RESULT ON  SOME     BIG  DATA SET")
        interpolation=[]
        for  chain in chain_order_list:
            #print(self.get_chunck(chain[0],chain[1]))
            interpolation.append(self.MLH(chain[0],chain[1]))
        if  len(lambda_list)!=chain_order_list[0][1]:
            print(" crazy   dude")
        else:
            w_average=0
            for  i in range(0,len(lambda_list)):
                w_average=w_average+(lambda_list[i]*interpolation[i])
                
                
        return [interpolation,w_average]
