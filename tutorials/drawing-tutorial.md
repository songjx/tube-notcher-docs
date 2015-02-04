# SolidWorks Drawings + Custom Property Templates Guide 

One more tutorial! This one's easy, I promise. I've set up several templates for our tube notcher drawings. These templates will make it much easier for us to make consistent, logical part and assembly drawings in Solidworks.

This tutorial will also show you why you don't have to give all your parts and assemblies super descriptive file names like `fixturing-vise-subassembly-jaw-extension-top-screw.SLDPRT`. Assembly, subassembly, material, finish, thread, weight, and misc other information can all be handled much better using custom properties.

## Setup

Some of the template files are SolidWorks custom property templates. There's one each for assemblies, parts, and drawings. We need to install them in the right folder so SolidWorks can find them. Do this on every computer you work at. Go to Options to find out where this folder is: 

![drawing-tutor##](https://s3.amazonaws.com/tube-notcher/drawing-tutorial/drawing-tutor01.png)

![drawing-tutor##](https://s3.amazonaws.com/tube-notcher/drawing-tutorial/drawing-tutor02.png)

Once you know the Custom Property Files location, copy and paste the three template files from our Git repo...

![drawing-tutor##](https://s3.amazonaws.com/tube-notcher/drawing-tutorial/drawing-tutor03.png)

...to that location. 

![drawing-tutor##](https://s3.amazonaws.com/tube-notcher/drawing-tutorial/drawing-tutor04.png)

## Using our custom property template for assemblies

Open an assembly file and the Custom Properties pane tab:

![drawing-tutor##](https://s3.amazonaws.com/tube-notcher/drawing-tutorial/drawing-tutor05.png)

Because we installed the custom property templates, the assembly property template automatically appears. Under `Description`, give the assembly a proper, pretty name. This will appear on the final drawing. Under `NextAssembly1`, specify what subassembly the current assembly is used in. This is the next level higher on the assembly hierarchy. Use `NextAssembly2` and `NextAssembly3` if the current assembly appears in more than one subassembly on the same level. 

Finally, choose the proper subsystem from the dropdown.

![drawing-tutor##](https://s3.amazonaws.com/tube-notcher/drawing-tutorial/drawing-tutor06.png)

## Making an assembly drawing

Make a drawing from the assembly: 

![drawing-tutor##](https://s3.amazonaws.com/tube-notcher/drawing-tutorial/drawing-tutor07.png)

Browse for our drawing template: 

![drawing-tutor##](https://s3.amazonaws.com/tube-notcher/drawing-tutorial/drawing-tutor09.png)

Once you place a drawing view of the model, some fields in the title block automatically populate with the custom properties entered previously. 

![drawing-tutor##](https://s3.amazonaws.com/tube-notcher/drawing-tutorial/drawing-tutor10.png)

## Using our custom property template for drawings

If you open the Custom Properties pane tab again, the fields from our drawings custom property template file show up. Use them to say who you are, make comments, mess with the revision number...

![drawing-tutor##](https://s3.amazonaws.com/tube-notcher/drawing-tutorial/drawing-tutor11.png)

## Using our custom property template for parts

If we go back to the vise assembly, select any part, and open the Custom Properties pane tab, the fields from the parts custom property template file show up. Here, the `body` is selected. I've given it a pretty name. The material field was automatically filled by the material I chose when I made the part. The weight is automatically calulated. Pin the task pane down if you'll be editing a bunch of parts in a row.

![drawing-tutor##](https://s3.amazonaws.com/tube-notcher/drawing-tutorial/drawing-tutor12.png)

I've selected a McMaster screw here. The file name for this one is especially ugly, so the description is even more useful. `IsFastener` is checked so that the screw will display properly in section view drawings. 

![drawing-tutor##](https://s3.amazonaws.com/tube-notcher/drawing-tutorial/drawing-tutor14.png)

You can select many parts at once to batch edit them. This is nice for the `NextAssembly` properties. 

![drawing-tutor##](https://s3.amazonaws.com/tube-notcher/drawing-tutorial/drawing-tutor15.png)

## Bill of Materials

If you include a Bill of Materials in your assembly drawings, the `DESCRIPTION` column automatically fills with your pretty `Description` names. You can also add a column for whatever other custom property name you want. Screw threads and lengths might be a good choice.

![drawing-tutor##](https://s3.amazonaws.com/tube-notcher/drawing-tutorial/drawing-tutor16.png)

## Bonus 

As a bonus, the `Description` property is now available as a column in Windows Explorer! To get it, right click the column headers...

![drawing-tutor##](https://s3.amazonaws.com/tube-notcher/drawing-tutorial/drawing-tutor20.png)

There will probably be two `Description` entries - one from Windows, and one from SolidWorks. The SolidWorks one is probably the second one.

![drawing-tutor##](https://s3.amazonaws.com/tube-notcher/drawing-tutorial/drawing-tutor18.png)

Pretty names! Now we can separate file names and part descriptions without getting confused in Windows Explorer. The only problem with this is that the `Description` entry doesn't seem to show up for any file that's currently open in SolidWorks. Not sure why.

![drawing-tutor##](https://s3.amazonaws.com/tube-notcher/drawing-tutorial/drawing-tutor19.png)