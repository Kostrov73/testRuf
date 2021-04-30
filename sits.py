from scrollLabel import ScrollLabel

class Sits(ScrollLabel):
    def __init__(self,total,**kwarg):
        self.current=0
        self.total=total
        text="Осталось " + str(self.total)+" приседаний"
        super().__init__(text,**kwarg)

    def next(self, *args):
        self.current+=1
        self.remain=max(0, self.total - self.current)
        text="Осталось "+str(self.remain)+" приседаний"
        super().set_text(text)