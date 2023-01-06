import model
import view
import for_teach

def button_clink():
    status=view.get_value()
    sername=view.get_value2()
    model.init(status,sername)
    if status=="t":
        result=model.sum()
        for_teach.run(result)
    elif status=='s':
        sobjet=view.get_value3()
        model.init2(sobjet)
        result2=model.sum2()
        view.view_data2(result2)
    #sername=model.run()
    #result3=for_teach.run()
    #result2=model.sum2()
    #view.view_data(result2)
    #view.view_data2(result3)