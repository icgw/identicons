from identicons import Identicon

# Set Your User id
id = "Hello"
# Initial an icon. Identicon(id, GridSize = 60, BackGround = "#f0f0f0")
demo = Identicon(id)
# Generate the icon
demo.generate()
# Show the icon
demo.show()
# Output the icon (PNG) to the current derectory. filename is id.png.
demo.output()
