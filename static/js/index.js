$(function () {

    //Close sidebar
    $("#close-nav").click(closeSidebar);
    $("#overlay").click(closeSidebar);

    //Toggle sidebar
    $("#open-menu").click(openSidebar);

    function closeSidebar() {
        $("#sidebar").removeClass("open");
        $("#overlay").removeClass("opaque");
    }

    function openSidebar() {
        $("#sidebar").addClass("open");
        $("#overlay").addClass("opaque");
        logEvent("UI", "Open Menu")
    }
});
