import java.io.File;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import ch.uzh.ifi.seal.changedistiller.ChangeDistiller;
import ch.uzh.ifi.seal.changedistiller.ChangeDistiller.Language;
import ch.uzh.ifi.seal.changedistiller.distilling.FileDistiller;
import ch.uzh.ifi.seal.changedistiller.model.entities.SourceCodeChange;




public class change {
    static List<File> file_v1 = new ArrayList<>();
    static List<File> file_v2 = new ArrayList<>();
    static int cou=0;
    public static void storeFiles(File[] files) {
    	
    	for(File fname:files) {
    		if(fname.isDirectory()) {
    			storeFiles(fname.listFiles());
    		}
    		else {
    			if(cou==0) {
    				file_v1.add(fname);
    			}
    			else {
    				file_v2.add(fname);
    			}
    			
    		}
    	}
    }
    
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		File[] files_v1  = new File("C:\\Users\\BITS-PC\\Downloads\\PROMISE\\PROMISE\\src\\ant-1.3").listFiles(); 
		File[] files_v2  = new File("C:\\Users\\BITS-PC\\Downloads\\PROMISE\\PROMISE\\src\\ant-1.4").listFiles();
		storeFiles(files_v1);
		cou++;
		storeFiles(files_v2);
		
		Collections.sort(file_v1);
		Collections.sort(file_v2);
		
		
		List<String> changed_files_v1 = new ArrayList<>();
		List<String> changed_files_v2 = new ArrayList<>();
        List<String> fnames = new ArrayList<>();
		int i=0,j=0;
		while(i!=file_v1.size()&&j!=file_v2.size()) {
			String s1 = file_v1.get(i).getName();
			String s2 = file_v2.get(j).getName();
			
			//System.out.println(s1);
			//System.out.println(s2);
			//System.out.println(s1.compareTo(s2));

			if(s1.compareToIgnoreCase(s2)<0) {
				i++;
			}
			else if(s1.compareToIgnoreCase(s2)>0) {
				j++;
			}
			else {
				changed_files_v1.add(file_v1.get(i).getAbsolutePath());
				changed_files_v2.add(file_v2.get(j).getAbsolutePath());
				fnames.add(file_v1.get(i).getName());

				i++;
				j++;
			}
		}
		for(int it=0;it<changed_files_v1.size();it++) {
		String f1 = changed_files_v1.get(it);
		String f2 = changed_files_v2.get(it);
		String name = fnames.get(it);
		//System.out.println(name);
		//System.out.println(f);

		if(f1.substring(f1.length()-5).equals(".java")&&f2.substring(f2.length()-5).equals(".java")) {
  		//File left = new File(f1);
		//File right = new File(f2);
        File left = new File("C:\\Users\\BITS-PC\\changedistiller\\resources\\testdata\\src_change\\TestLeft.java");
        File right = new File("C:\\Users\\BITS-PC\\changedistiller\\resources\\testdata\\src_change\\TestRight.java");

		FileDistiller distiller = ChangeDistiller.createFileDistiller(Language.JAVA);
		try {
		    distiller.extractClassifiedSourceCodeChanges(left, right);
		} catch(Exception e) {
		    /* An exception most likely indicates a bug in ChangeDistiller. Please file a
		       bug report at https://bitbucket.org/sealuzh/tools-changedistiller/issues and
		       attach the full stack trace along with the two files that you tried to distill. */
		    System.err.println("Warning: error while change distilling. " + e.getMessage());
		}

		List<SourceCodeChange> changes = distiller.getSourceCodeChanges();
		if(changes != null) {
			String loc = "C:\\Users\\BITS-PC\\Desktop\\Editscript\\" + name + "_changes.txt" ;
            Path path = Paths.get(loc);
            String content = "";
		    for(SourceCodeChange change : changes) {
		        // see Javadocs for more information
		    	
		        //content += change.toString()+"\n"+change.getChangedEntity().toString() + " " + change.getChangeType().toString() + "\n";
	            System.out.println(change.toString());
		    	System.out.println(change.getChangedEntity().toString());
	            System.out.println(change.getParentEntity().toString());
	            System.out.println(change.getRootEntity());
	            System.out.println(change.getChangeType().toString());
	            System.out.println("===============================");

	            


	            
		    }
		    /*try {
				Files.write(path, content.getBytes(StandardCharsets.UTF_8));
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}*/
		}
		}

	}
	}
}
