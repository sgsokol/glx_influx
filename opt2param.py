# 2020-03-30 sokol@insa-toulouse.fr
# code to execute after OptionParser.parser definition in some python code
# it will print out a series of <param> tags to be finished by hands
import html
def isfloat(value):
  try:
    float(str(value))
    return True
  except ValueError:
    return False
def isstring(value):
    return (type(value) == type(""))
print('<section name="opt" title="Advanced Options" expanded="false">')
for opt in parser.option_list:
    # write portion of the galaxy command for this option to stderr
    sys.stderr.write(f'  #if $opt.{opt.get_opt_string()[2:]}:\n    {opt.get_opt_string()}'+(f"='$opt.{opt.get_opt_string()[2:]}'" if opt.takes_value() else "")+'\n  #end if\n')
    if opt.type == "choice":
        print(f'  <param argument="{opt.get_opt_string()}" type="select" label="{opt.get_opt_string()}" optional="true" help="{html.escape(opt.help)}">')
        for ch in opt.choices:
            print(f'    <option value="{ch}">{ch}</option>')
        print('  </param>')
    elif opt.type == "int":
        print(f'  <param argument="{opt.get_opt_string()}" type="integer" value="{opt.default if str(opt.default).isdigit() else ""}" label="{opt.get_opt_string()}" optional="true" help="{html.escape(opt.help)}" />')
    elif opt.type == "float":
        print(f'  <param argument="{opt.get_opt_string()}" type="float" value="{opt.default if isfloat(opt.default) else ""}" label="{opt.get_opt_string()}" optional="true" help="{html.escape(opt.help)}" />')
    elif opt.type == "string":
        print(f'  <param argument="{opt.get_opt_string()}" type="text" value="{opt.default if isstring(opt.default) else ""}" label="{opt.get_opt_string()}" optional="true" help="{html.escape(opt.help)}" />')
    elif opt.type is None:
        if opt.action == "store_true" or opt.action == "version" or opt.action == "help":
            print(f'  <param argument="{opt.get_opt_string()}" type="boolean" checked="false" truevalue="TRUE" falsevalue="FALSE" label="{opt.get_opt_string()}" optional="true" help="{html.escape(opt.help)}" />')
        else:
            print(f'  <param argument="{opt.get_opt_string()}" type="text" value="?" label="{opt.get_opt_string()}" optional="true" help="{html.escape(opt.help)}" />')
    else:
        print(f'  <param argument="{opt.get_opt_string()}" type="text"'+(f' value="??"' if opt.takes_value() else "")+f' label="{opt.get_opt_string()}" optional="true" help="{html.escape(opt.help)}" />')
print('</section>')
exit(0)
