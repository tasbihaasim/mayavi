from enthought.traits.ui.api import View, HGroup, Item
from enthought.tvtk.tvtk_base import TVTKBaseHandler
    
view = View((['generate_texture_coordinates'], ['scalar_mode'],
    HGroup(Item('u_resolution', label = 'u'), 
          Item('v_resolution', label = 'v'),
          Item('w_resolution', label = 'w'),
          label = 'Resolution', show_border = True)),
    Item('handler.advanced_view'),
    handler = TVTKBaseHandler,
    title='Edit ParametricFunctionSource properties', scrollable=True,
    buttons=['OK', 'Cancel'])
    
