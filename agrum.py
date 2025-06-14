import pyagrum as gum
import pyagrum.lib.image
import pyagrum.lib.bn2graph as gumb2g
import pyagrum.lib.image as gumimage
import pyagrum.lib.explain as explain
import pyagrum.lib.notebook as gnb
import imgkit
from IPython.display import display, HTML
from cairosvg import svg2png


def learn(data, age_labels, salary_values, exp_values):
    template = get_template(age_labels, salary_values, exp_values)
    learner = gum.BNLearner(data, template)
    bn = learner.addMandatoryArc("Gender", "PhD").addMandatoryArc("PhD", "Salary").addMandatoryArc("Gender", "Salary").addMandatoryArc("Age-group", "Salary").addMandatoryArc("Age-group", "XP").addMandatoryArc("Age-group", "PhD").addMandatoryArc("XP", "Salary").addMandatoryArc("Gender", "Salary").learnBN()
    gumimage.export(bn, "out/bn-learned.png")

    #explain.showInformation(bn, {}, size="20")
    inf= explain.getInformation(bn, {}, size="20")

    Func = open("out/learned-entropy.html", "w", encoding="utf-8")
    Func.write(inf)
    Func.close()
    #gnb.showInference(bn)
    svg=gnb.getInference(bn)
    svg2png(bytestring=svg, write_to='out/inference.png')
    #display(HTML(inf))

    #imgkit.from_file(inf, 'out/out.jpg')



def get_template(age_labels, salary_values, exp_values):
    #print(salary_values.sort())
    template = gum.BayesNet("dummy")

    PhD=template.add(gum.LabelizedVariable("PhD", "PhD", 2))
    Age=template.add(gum.LabelizedVariable("Age-group", "Age-group", age_labels))
    Gender=template.add(gum.LabelizedVariable("Gender", "Gender", ["Female", "Male","Other"]))
    Salary=template.add(gum.IntegerVariable("Salary", "Salary", salary_values))
    XP=template.add(gum.IntegerVariable("XP", "XP", exp_values))

    #template.addNoChildrenNode(*args)
    #template.addArc(XP, Salary)

    #pyagrum.lib.image.BN2dot(template)
    #graph = gumb2g.BN2dot(template)

    gumimage.export(template, "out/template.png")
    return template





    #pyagrum.lib

    #gum.show(template)