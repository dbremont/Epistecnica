# X11 Opcodes

> 🧠 Many opcodes above support replies or events, depending on the command.
⚙️ For extensions, the server uses QueryExtension (opcode 98) to allocate a dynamic major opcode. Extension opcodes start there and must be resolved per extension.
> 

| Opcode | Request Name | Description |
| --- | --- | --- |
| 1 | `CreateWindow` | Creates a window. |
| 2 | `ChangeWindowAttributes` | Changes window attributes like event masks. |
| 3 | `GetWindowAttributes` | Retrieves attributes of a window. |
| 4 | `DestroyWindow` | Destroys a window. |
| 5 | `DestroySubwindows` | Destroys all subwindows. |
| 6 | `ChangeSaveSet` | Modifies the save-set for a client. |
| 7 | `ReparentWindow` | Changes a window's parent. |
| 8 | `MapWindow` | Maps (shows) a window. |
| 9 | `MapSubwindows` | Maps all subwindows. |
| 10 | `UnmapWindow` | Unmaps (hides) a window. |
| 11 | `UnmapSubwindows` | Unmaps all subwindows. |
| 12 | `ConfigureWindow` | Changes window geometry (size, position, stacking). |
| 13 | `CirculateWindow` | Changes stacking order. |
| 14 | `GetGeometry` | Retrieves geometry of a drawable (window or pixmap). |
| 15 | `QueryTree` | Gets the window hierarchy. |
| 16 | `InternAtom` | Creates or returns an atom identifier. |
| 17 | `GetAtomName` | Returns the name for an atom. |
| 18 | `ChangeProperty` | Sets a property on a window. |
| 19 | `DeleteProperty` | Deletes a property from a window. |
| 20 | `GetProperty` | Gets a property from a window. |
| 21 | `ListProperties` | Lists all properties of a window. |
| 22 | `SetSelectionOwner` | Sets the owner of a selection. |
| 23 | `GetSelectionOwner` | Gets the current owner of a selection. |
| 24 | `ConvertSelection` | Requests conversion of selection data. |
| 25 | `SendEvent` | Sends a synthetic event. |
| 26 | `GrabPointer` | Grabs the pointer. |
| 27 | `UngrabPointer` | Releases pointer grab. |
| 28 | `GrabButton` | Grabs a pointer button. |
| 29 | `UngrabButton` | Releases a grabbed button. |
| 30 | `ChangeActivePointerGrab` | Modifies the active pointer grab. |
| 31 | `GrabKeyboard` | Grabs the keyboard. |
| 32 | `UngrabKeyboard` | Releases keyboard grab. |
| 33 | `GrabKey` | Grabs a key on the keyboard. |
| 34 | `UngrabKey` | Releases a grabbed key. |
| 35 | `AllowEvents` | Allows or disallows event processing. |
| 36 | `GrabServer` | Grabs the server (locks out other clients). |
| 37 | `UngrabServer` | Releases server grab. |
| 38 | `QueryPointer` | Queries pointer location and status. |
| 39 | `GetMotionEvents` | Returns pointer motion history. |
| 40 | `TranslateCoordinates` | Translates coordinates between windows. |
| 41 | `WarpPointer` | Moves the pointer. |
| 42 | `SetInputFocus` | Sets input focus to a window. |
| 43 | `GetInputFocus` | Gets input focus window. |
| 44 | `QueryKeymap` | Returns the keyboard keymap. |
| 45 | `OpenFont` | Opens a font. |
| 46 | `CloseFont` | Closes a font. |
| 47 | `QueryFont` | Returns font metrics. |
| 48 | `QueryTextExtents` | Gets character dimensions in a font. |
| 49 | `ListFonts` | Lists available fonts. |
| 50 | `ListFontsWithInfo` | Lists fonts with detailed info. |
| 51 | `SetFontPath` | Sets the font search path. |
| 52 | `GetFontPath` | Gets the font search path. |
| 53 | `CreatePixmap` | Creates an off-screen image buffer. |
| 54 | `FreePixmap` | Frees a pixmap. |
| 55 | `CreateGC` | Creates a graphics context. |
| 56 | `ChangeGC` | Changes properties of a GC. |
| 57 | `CopyGC` | Copies a graphics context. |
| 58 | `SetDashes` | Sets dash pattern for lines. |
| 59 | `SetClipRectangles` | Sets clipping rectangles for drawing. |
| 60 | `FreeGC` | Frees a graphics context. |
| 61 | `ClearArea` | Clears a portion of a window. |
| 62 | `CopyArea` | Copies part of a drawable to another. |
| 63 | `CopyPlane` | Copies single-bit plane of drawable. |
| 64 | `PolyPoint` | Draws points. |
| 65 | `PolyLine` | Draws lines. |
| 66 | `PolySegment` | Draws segments. |
| 67 | `PolyRectangle` | Draws rectangles. |
| 68 | `PolyArc` | Draws arcs. |
| 69 | `FillPoly` | Draws filled polygons. |
| 70 | `PolyFillRectangle` | Draws filled rectangles. |
| 71 | `PolyFillArc` | Draws filled arcs. |
| 72 | `PutImage` | Writes image data to drawable. |
| 73 | `GetImage` | Reads image data from drawable. |
| 74 | `PolyText8` | Draws text (8-bit). |
| 75 | `PolyText16` | Draws text (16-bit). |
| 76 | `ImageText8` | Draws image-based text (8-bit). |
| 77 | `ImageText16` | Draws image-based text (16-bit). |
| 78 | `CreateColormap` | Creates a colormap. |
| 79 | `FreeColormap` | Frees a colormap. |
| 80 | `CopyColormapAndFree` | Copies a colormap and frees source. |
| 81 | `InstallColormap` | Installs a colormap. |
| 82 | `UninstallColormap` | Uninstalls a colormap. |
| 83 | `ListInstalledColormaps` | Lists installed colormaps. |
| 84 | `AllocColor` | Allocates a color in a colormap. |
| 85 | `AllocNamedColor` | Allocates a named color. |
| 86 | `AllocColorCells` | Allocates read/write color cells. |
| 87 | `AllocColorPlanes` | Allocates color planes. |
| 88 | `FreeColors` | Frees allocated color cells. |
| 89 | `StoreColors` | Sets color values. |
| 90 | `StoreNamedColor` | Sets named color. |
| 91 | `QueryColors` | Gets current color values. |
| 92 | `LookupColor` | Looks up RGB values for a named color. |
| 93 | `CreateCursor` | Creates a cursor. |
| 94 | `CreateGlyphCursor` | Creates a glyph-based cursor. |
| 95 | `FreeCursor` | Frees a cursor. |
| 96 | `RecolorCursor` | Changes colors of a cursor. |
| 97 | `QueryBestSize` | Gets best size for certain objects. |
| 98 | `QueryExtension` | Checks if an extension is supported. |
| 99 | `ListExtensions` | Lists all supported extensions. |
| 100 | `ChangeKeyboardMapping` | Changes keyboard map. |
| 101 | `GetKeyboardMapping` | Gets current keyboard map. |
| 102 | `ChangeKeyboardControl` | Changes keyboard settings. |
| 103 | `GetKeyboardControl` | Gets keyboard settings. |
| 104 | `Bell` | Rings the bell. |
| 105 | `ChangePointerControl` | Changes pointer settings. |
| 106 | `GetPointerControl` | Gets pointer settings. |
| 107 | `SetScreenSaver` | Sets screen saver parameters. |
| 108 | `GetScreenSaver` | Gets screen saver parameters. |
| 109 | `ChangeHosts` | Modifies access control list. |
| 110 | `ListHosts` | Lists current access control hosts. |
| 111 | `SetAccessControl` | Enables/disables access control. |
| 112 | `SetCloseDownMode` | Controls resource release at client close. |
| 113 | `KillClient` | Forcibly closes a client. |
| 114 | `RotateProperties` | Reorders window properties. |
| 115 | `ForceScreenSaver` | Forces screen saver state. |
| 116 | `SetPointerMapping` | Sets pointer button mapping. |
| 117 | `GetPointerMapping` | Gets pointer button mapping. |
| 118 | `SetModifierMapping` | Sets keyboard modifier mapping. |
| 119 | `GetModifierMapping` | Gets keyboard modifier mapping. |
| 127 | `NoOperation` | Does nothing (ping, padding). |

## References

- [https://www.x.org/releases/current/doc/xproto/x11protocol.html](https://www.x.org/releases/current/doc/xproto/x11protocol.html)