---
tags: [principle]
---

# UI/UX Checklist


> aka. Sugerencia.
> 

## 🧱 **Layout & Structure**

- [ ]  Consistent grid system and spacing scale
- [ ]  Responsive layout (desktop, tablet, mobile, ultra-wide)
- [ ]  Consistent padding and margins across components
- [ ]  Clear visual hierarchy using size, color, contrast, and grouping
- [ ]  Adaptive components (e.g. cards, modals, tables)
- [ ]  Flexibility for localization and right-to-left (RTL) languages
- [ ]  Use of whitespace to reduce cognitive load
- [ ]  Progressive Disclosure: show complexity progressively

## 🎨 **Visual Design**

- [ ]  Unified visual theme and brand consistency
- [ ]  Accessible color contrast (text, icons, buttons)
- [ ]  Scalable typography (modular scale, rem units)
- [ ]  Iconography is meaningful, consistent, and accessible
- [ ]  Smooth and meaningful animations/transitions
- [ ]  Dark/Light mode support with auto-detection
- [ ]  Visual feedback for hover, click, focus, loading
- [ ]  Clear disabled and active states

## 🧭 **Navigation**

- [ ]  Primary navigation is prominent and persistent
- [ ]  Secondary/contextual navigation is discoverable
- [ ]  Logical page hierarchy and structure
- [ ]  Breadcrumbs for deep navigation
- [ ]  Sticky headers/footers as needed
- [ ]  URL reflects current view/state
- [ ]  Navigation works with browser history (Back/Forward)
- [ ]  Keyboard and screen reader accessible
- [ ]  Mobile-friendly menu (hamburger, bottom nav)
- [ ]  Consistent location and labeling of navigation elements

## 🔍 **Search & Filtering**

- [ ]  Predictive search/autocomplete
- [ ]  Semantic search (e.g., natural language queries)
- [ ]  Fuzzy matching and error tolerance
- [ ]  Filters are intuitive, accessible, and resettable
- [ ]  Search results are ranked and relevant
- [ ]  Support for advanced search (e.g., filters, operators)
- [ ]  Search suggestions and recent history

## 🧠 **User Assistance & Guidance**

- [ ]  Onboarding flow for new users
- [ ]  Tooltips, popovers, and contextual help
- [ ]  Empty states with explanations and actions
- [ ]  Visual cues for guidance (progress indicators, hotspots)
- [ ]  Walkthroughs, hints, or coachmarks
- [ ]  Command assistant / Copilot (if complex domain)
- [ ]  Support for intelligent recommendations
- [ ]  Inline documentation or expandable help for complex fields

## 🛠️ **Forms & Inputs**

- [ ]  Label all inputs clearly and persistently
- [ ]  Input type matches expected data (e.g., `type="email"`)
- [ ]  Inline validation (real-time, clear errors)
- [ ]  Helpful error messages (not just "Invalid input")
- [ ]  Smart defaults and pre-filled values
- [ ]  Auto-correction and input masking
- [ ]  Dynamic form sections (conditional fields)
- [ ]  Tab order and keyboard navigation
- [ ]  Support for batch actions and bulk creation
- [ ]  Inline creation of new items/entities
- [ ]  File upload with progress, preview, drag-and-drop
- [ ]  Autosave + edit-in-place support
- [ ]  Form reset, undo/redo support
- [ ]  Multi-step forms with clear progression

## 🖱️ **Interaction & Usability**

- [ ]  Clear affordance for interactive elements (e.g., buttons look clickable)
- [ ]  Minimum target size (44px on touch devices)
- [ ]  Feedback for all interactions (hover, active, focus)
- [ ]  Consistent placement of actions (top-right, bottom-right, etc.)
- [ ]  Accessible tooltips and labels
- [ ]  Drag-and-drop supported where it improves UX
- [ ]  Resizable and reorderable lists/tables (if needed)
- [ ]  Keyboard shortcuts for frequent actions
- [ ]  Customizable UI layout or themes (if applicable)

## ⚠️ **Error Handling & Feedback**

- [ ]  Descriptive and user-friendly error messages
- [ ]  Prevent errors through constraints, defaults, confirmations
- [ ]  Visual feedback for success/failure/loading states
- [ ]  Status indicators (e.g., saving, syncing, offline)
- [ ]  Global or inline alert components
- [ ]  Undo functionality for destructive actions
- [ ]  Non-blocking, dismissible notifications
- [ ]  Retry actions for failed operations

## 📱 **Mobile Optimization**

- [ ]  Responsive/adaptive layout for all screen sizes
- [ ]  Touch-friendly targets (min 44x44px)
- [ ]  Avoid fixed dimensions or overflow issues
- [ ]  Mobile keyboards don't cover inputs
- [ ]  Native gestures respected (swipe, tap, drag)
- [ ]  Safe areas respected (notch, home indicators)

## 🧑‍🦽 **Accessibility (A11y)**

- [ ]  Semantic HTML used properly
- [ ]  ARIA roles and labels for assistive tech
- [ ]  Keyboard-navigable interface
- [ ]  Focus indicators are visible and consistent
- [ ]  Screen reader-friendly layout and interaction
- [ ]  Skip links and logical tab order
- [ ]  Colorblind-safe palette options
- [ ]  No reliance on color alone to convey meaning
- [ ]  All dynamic content is announced via ARIA live regions

## ⏱️ **Performance & Reliability**

- [ ]  Fast load times (<2 seconds)
- [ ]  Lazy loading for images, videos, and lists
- [ ]  Optimized assets (compressed SVG, WebP, etc.)
- [ ]  Minimal layout shift (avoid cumulative layout shift)
- [ ]  Reliable behavior across all devices and browsers
- [ ]  Graceful degradation and offline support (if needed)
- [ ]  Optimistic UI updates for responsiveness

## 🧪 **Testing & QA**

- [ ]  Cross-browser testing (Chrome, Firefox, Safari, Edge)
- [ ]  Cross-device testing (mobile, tablet, desktop)
- [ ]  Accessibility tested (axe, Lighthouse, NVDA, etc.)
- [ ]  Usability testing with users or internal QA
- [ ]  Automated tests for components and flows
- [ ]  No broken links, missing images, or JavaScript errors
- [ ]  Regression testing for critical paths

## 📋 **Content & Copy**

- [ ]  Clear, concise, jargon-free language
- [ ]  Consistent tone and style
- [ ]  Content hierarchy matches visual hierarchy
- [ ]  Error messages explain the problem and solution
- [ ]  Placeholder text is not used as a label
- [ ]  Support for localization and pluralization
- [ ]  Microcopy supports usability (button labels, tooltips, etc.)

## 🤖 **Intelligent UX Tools**

- [ ]  Predictive/autocomplete input for known entities
- [ ]  Semantic search or natural language query parsing
- [ ]  Auto-correction and typo detection
- [ ]  Command palette / assistant / Copilot UI
- [ ]  AI-powered suggestions (e.g., product recommendations, shortcuts)
- [ ]  Learning from user behavior (recent history, smart defaults)

## References

- https://dribbble.com/tags/checklist
- https://designsystemsrepo.com/tools/
- https://shiftnudge.com/checklist
- https://www.checklist.design/
- https://www.reddit.com/r/FigmaDesign/comments/13l6own/making_a_ui_kit_is_there_a_good_checklist_for/
- https://www.smashingmagazine.com/2022/09/ux-checklists-for-interface-designers/
- https://www.designsystemchecklist.com/