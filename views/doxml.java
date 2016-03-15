import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class doxml{

	public static void main(String[]args)throws IOException{

		for(int i = 0; i < args.length; i++){

			String ruta = args[i];
			String nombre = args[i];
			String mayusc = args[i].substring(0,1).toUpperCase()+args[i].substring(1,args[i].length());
			File archivo = new File(ruta+".xml");
			BufferedWriter bw;
			if(archivo.exists()) {
				bw = new BufferedWriter(new FileWriter(archivo));
				System.out.println("El archivo ya esta creado");
			} else {
				bw = new BufferedWriter(new FileWriter(archivo));
				String var = "ventas";
				String str = "<?xml version='1.0' encoding='UTF-8'?>\n"+
"<openerp>\n"+
"    <data>\n"+
"        <!-- window action -->\n"+
"        <!--\n"+
"            The following tag is an action definition for a 'window action',\n"+
"            that is an action opening a view or a set of views\n"+
"        -->\n"+
"        <!-- Action to open "+nombre+" -->\n"+
"        <act_window \n"+
"            id='do_"+nombre+"_action' \n"+
"            name='"+mayusc+"s' \n"+
"            res_model='"+var+"."+nombre+"' \n"+
"            view_mode='tree,form,search'/>\n"+
"\n"+
"        <menuitem \n"+
"            id='second_left_menu_"+nombre+"' \n"+
"            name='"+mayusc+"s' \n"+
"            parent='first_left_menu' \n"+
"            action='do_"+nombre+"_action'/>\n"+
"        <!-- Full id location:\n"+
"             action='openacademy.course_list_action'\n"+
"             It is not required when it is the same module -->\n"+
"\n"+
"        <!-- view -->\n"+
"        <record id='view_form_"+nombre+"' model='ir.ui.view'>\n"+
"            <field name='name'>"+nombre+" Form</field>\n"+
"            <field name='model'>"+var+"."+nombre+"</field>\n"+
"            <field name='arch' type='xml'>\n"+
"            <form>\n"+
"                <header>\n"+
"                </header>\n"+
"                <sheet>\n"+
"                <group name='group_top'>\n"+
"                    <group name='group_left'>\n"+     
"\n"+
"                        <field name='' placeholder=''/>\n"+
"\n"+
"                    </group>\n"+
"                </group>\n"+
"                </sheet>\n"+
"            </form>\n"+
"            </field>\n"+
"        </record>\n"+
"\n"+
"        <!-- Tree -->\n"+
"        <record id='view_tree_"+nombre+"' model='ir.ui.view'>\n"+
"            <field name='name'>"+nombre+" Tree</field>\n"+
"            <field name='model'>"+var+"."+nombre+"</field>\n"+
"            <field name='arch' type='xml'>\n"+
"            <tree>\n"+
"\n"+
"                    <field name=''/>\n"+
" \n"+
"            </tree>\n"+
"            </field>\n"+
"        </record>\n"+
"    </data>\n"+
"</openerp>";
				bw.write(str);
			}
			bw.close();
			try {
				Runtime.getRuntime().exec("subl "+ruta+".xml");
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}
}