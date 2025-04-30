import adsk.core, adsk.fusion, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        if not design:
            ui.messageBox('No active Fusion design', 'No Design')
            return

        # Get the root component of the active design.
        rootComp = design.rootComponent
        
        # Create the title for the output.
        resultString = '\nMODEL HIERARCHY:\n' + '='*20 + '\n' + design.parentDocument.name + '\n' + '='*20 + '\n\n'

        # Iterate through all of the occurrences in the assembly.
        for i in range(0, rootComp.allOccurrences.count):
            occ = rootComp.allOccurrences.item(i)   
            resultString += occ.component.name + '\n'     
         

        # Display the result.
        # Write the results to the TEXT COMMANDS window.
        textPalette = ui.palettes.itemById('TextCommands')
        if not textPalette.isVisible:
            textPalette.isVisible = True
        textPalette.writeText(resultString)
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
