// // // frappe.ui.form.on("details", {

// // //     validate(frm) {
// // //         if (String(frm.doc.phone).length !== 10) {
// // //             frappe.throw("Phone number must contain exactly 10 digits.");
// // //         }
// // //     },
// // //     timeline_refresh(frm) 
// // //     {
// // //         frappe.msgprint("Timeline Refreshed");
// // //     }

// // // });
// // // frappe.ui.form.on("details", {
// // //     refresh(frm) {
// // //         console.log("Client Script Loaded");
// // //     },

// // //     timeline_refresh(frm) {
// // //         console.log("Timeline Refresh Triggered");
// // //         frappe.msgprint("Timeline Refreshed");
// // //     }
// // // });
// // // frappe.ui.form.on("details", {
// // //     after_save(frm){
// // //         frm.set_value('name1',"cibin")
// // //         frm.set_df_property('phone','read_only',1)
// // //     },
// // //    refresh(frm) {

// // //        frm.add_custom_button("Check status",function(){
// // //         if(frm.is_dirty())
// // //         {
// // //             frappe.msgprint("Form has unsaved data")
// // //         }
// // //         else
        
// // //         {
// // //             frappe.msgprint("Form is already saved")
// // //         }
// // //        });

// // //     },
// // //         before_save(frm) {
// // //         frm.set_value(
// // //             "full",
// // //             frm.doc.name1 + " " + frm.doc.name2
// // //         );
// // //     }
// // // });
// // frappe.ui.form.on("details", {
// //     refresh(frm) {
// //         frm.call("get_message")
// //             .then(r => {
// //                 frappe.msgprint("Hello " + r.message);
// //             });
// //     }
// // });

// // });
// // frappe.ui.form.on("details", {
    
// //     refresh(frm) {
// //         if (frm.is_new()) {
// //             return;
// //         }   
// //         frm.call("get_message")
// //             .then(r => {
// //                 frappe.msgprint("Hello " + r.message);
// //             });

// //     }
// // });
// // frappe.ui.form.on("details",{
// //     before_save(frm){
// //         frm.set_value("fl",frm.doc.name1 +frm.doc.name2)
// //     },
// //     refresh(frm) {

// //         frm.add_custom_button("tongle", function () {
// //             frm.toggle_enable("check",true);
// //         });


// //     }
    
    
// // })
// .

// // ghloerjoblsn;nbn
// frappe.ui.form.on("details", {

//     // refresh(frm) {
//         // frm.add_custom_button("Default details", () => {
//         //     frm.call("create_new")
//         //         .then(() => {
//         //             frappe.msgprint("Default details are added");
//         //         });
//         // });

//         // if (!frm.is_new()) {
            // frm.add_custom_button("Delete the details", () => {
            //     frm.call("delete")
            //         .then(() => {
            //             frappe.msgprint("Successfully deleted");
            //             frappe.set_route("List", "details");
            //         });
            // });

//         //     frm.add_custom_button("check all box", () => {
//         //         frm.call("check_all")
//         //             .then(() => {
//         //                 frappe.msgprint("Successfully checked all box");
//         //                 frappe.set_route("List", "details");
//         //             });
//         //     });

//         //     frm.add_custom_button("uncheck all box", () => {
//         //         frm.call("uncheck_all")
//         //             .then(() => {
//         //                 frappe.msgprint("Successfully unchecked all box");
//         //                 frappe.set_route("List", "details");
//         //             });
//         //     });

//         //     frm.add_custom_button("rename", () => {
//         //         frm.call("rename")
//         //             .then(() => {
//         //                 frappe.msgprint("Successfully renamed");
//         //                 frappe.set_route("List", "details");
//         //             });
//         //     });
//         // };

//         // frm.add_custom_button("details of field", () => {
//         //     frm.call("details")
//         //         .then(r => {
//         //             frappe.msgprint(String(r.message));
//         //         });
//         // });
//     // },

//     // onload(frm) {
//     //     frm.call("last_doc")
//     //         .then(r => {
//     //             frappe.msgprint("Last created name: " + r.message);
//     //         });

//     //     frm.call("last_doc_order")
//     //         .then(r => {
//     //             frappe.msgprint("First created name: " + r.message);
//     //         });
//     // }

//  });
// frappe.ui.form.on("details", {
//     refresh(frm) {
//         frm.add_custom_button("Delete the details", () => {
//             frm.call("delete")
//                 .then(() => {
//                     frappe.msgprint("Successfully deleted");
//                     frappe.set_route("List", "details");
//                 });
//         });
//     }
// });

// frappe.ui.form.on("details",{
//     refresh(frm){
//         frm.add_custom_button("default name",()=>{
//             frm.call("default_save")
//         });
//         frm.add_custom_button("timeline",()=>{
//             frm.call("timeline")
//         });
//          frm.add_custom_button("see view",()=>{
//             frm.call("view")
//                 .then(r=>{
//                     console.log(r.message);
//                 })
//         });
//         frm.add_custom_button("add tag",()=>{
//             frm.call("add_tags")
                
//         });
//         frm.add_custom_button("view tag",()=>{
//             frm.call("ge_tags")
//                 .then(r=>{
//                     console.log(r.message)
//                     frappe.msgprint(JSON.stringify(r.message));
//                 })
//         });
//     },
//     onload(frm)
//     {
//         frm.call("get_titlee")
//             .then(r=>{
//                 frappe.msgprint("welcome "+r.message)
//             });
//        frm.call("add_users").then(() => {
//     frappe.msgprint("View added");
// });
     

//     }
// })
    // frappe.ui.form.on("details", {
    //     refresh(frm) {
    //         let wrapper = frm.fields_dict.dynamic_control.$wrapper;

    //         wrapper.empty();

    //         let control = frappe.ui.form.make_control({
    //             parent: wrapper,
    //             df: {
    //                 label: "Temporary Name",
    //                 fieldname: "temp_name",
    //                 fieldtype: "Data",
    //                 reqd: 1,
    //                 placeholder: "Enter Name"
    //             },
    //             render_input: true
    //         });
    //     }
    // });
    // frappe.ui.form.on("details",{
    //     refresh(frm){
    //         frm.add_custom_button("date formot",()=>{
    //             frm.call("date_format")
    //                 .then(r=>{
    //                     frappe.msgprint(r.message)
    //                 })
    //         })
    //     }
    // })
    // frappe.ui.form.on("details",{
    //     refresh(frm){
    //         frm.add_custom_button("find",()=>{
    //             frm.call("find")
    //                 .then(r=>{
    //                     frappe.msgprint(r.message)
    //                 }
    //                 )
    //         })
    //     }
    // })
    
    // frappe.ui.form.on("details",{
    //     refresh(frm){
    //         let d=new frappe.ui.Dialog({
    //     title :"enter details",
    //     fields:[
    //         {
    //             label:"name",
    //             fieldname:"nam2",
    //             fieldtype:"Data"
    //         }
    //     ],
    //     size:"large",
    //     primary_action_label:"sumbit",
    //     primary_action(value){
    //         d.hide();
    //     }
    // });
    //   d.show();
      
    //     }
    // })
    // frappe.ui.form.on("details",{
    //     onload(frm){
    //          frappe.msgprint({
    //             title:"welcome message",
    //             indicator:"orange",
    //             message:"weclome to frappe "
    //         })
    //     }
    // })
//    frappe.ui.form.on("details",{
//     refresh(frm){
//         frappe.show_alert({message:"shut up,okay?",                                                     
//             indicator:"green"

//         },20);

//     }}
//     )
// frappe.ui.form.on("details", {
//     refresh(frm) {

//         frm.add_custom_button("Scan Barcode", () => {

//             new frappe.ui.Scanner({
//                 dialog: true,
//                 multiple: false,

//                 on_scan(data) {
//                     frm.set_value("barcode", data.decodedText);
//                 }
//             });

//         });

//     }
// });
   
// frappe.ui.form.on("details",{
//     refresh(frm){
//         frm.add_custom_button("scanner",()=>{
//             new frappe.ui.Scanner({
//                 dialog:true,
//                 multiple:false,
//                 on_scan(data){
//                     frm.set_Value("barcode",data.decodedText);
//                 }
//             });
//         });
// //     }
// // })

// frappe.ui.form.on("details", {
//     refresh(frm) {
//         let d = new frappe.ui.Dialog({
//             title: "Input Box",
//             fields: [
//                 {
//                     label: "First Name",
//                     fieldname: "first_name",
//                     fieldtype: "Data"
//                 }
//             ],
//             primary_action_label: "Create Contact",

//             primary_action(values) {
//                 frappe.route_options = {
//                     subject: values.first_name
//                 };

//                 d.hide();

//                 frappe.new_doc("task");
//             }
//         });

//         d.show();
//     }
// });
// frappe.ui.form.on("details", {
//     refresh(frm) {
//         frappe.ui.form.make_control({
//             parent: frm.get_field("html_wpel").$wrapper,
//             df: {
//                 label: "Due Date",
//                 fieldname: "due_date",
//                 fieldtype: "Data"
//             },
//             render_input: true
//         });
//     }
// });
// frappe.ui.form.on("details",{
//     refresh(frm){
//         frappe.ui.make_control({
//             parent:frm.get_field("preview").$wrapper
//             wrapper.empty()
//             df:{

//             }
//         })
//     }
// })
// frappe.ui.form.on("details",{
//     start(frm){
//         if(frm.doc.start && frm.doc.end)
//         {
//         frm.call("caldate")
//         }
//     },
//      end(frm){
//         if(frm.doc.start && frm.doc.end)
//         {
//         frm.call("caldate")
//         }
//     }
// })  


// frappe.ui.form.on("details",{

//     before_save(frm) {
//         frm.call("creation");
//     }

// })

// frappe.ui.form.on("details", {
//     refresh(frm) {

        
//         let $wrapper = $("<div class='my-control'></div>");

       
//         $wrapper.appendTo(frm.$wrapper);

//         let due_date = frappe.ui.form.make_control({
//             parent: $wrapper,

//             df: {
//                 label: "Due Date",
//                 fieldname: "due_date",
//                 fieldtype: "Date"
//             },

//             render_input: true
//         });

    
//         due_date.set_value(frappe.datetime.get_today());

//         // Get the value
//         console.log("Due Date:", due_date.get_value());
//     }
// });

// frappe.ui.form.on("details",{
//     refresh(frm){
        // frm.add_custom_button("Scan Barcode", () => {

        //     new frappe.ui.Scanner({
        //         dialog: true,
        //         multiple: false,

        //         on_scan(data) {

        //             frm.set_value(
        //                 "barcode",
        //                 data.decodedText
        //             );

        //         }
        //     });

        // });
    //    frm.email_doc();
    // frm.email_doc(`hello ${frm.doc.name3}`)
//  frm.set_value("status", "Inactive").then(() => {
            // if (frm.dirty()) {
            //     frappe.show_alert("Please save the form first");
            // }
        // });


        
        // if(frm.doc.status==="Active"){
        //     frm.enable_save()
        // }
        // else{
        //     frm.disable_save()
        // }
    //   frm.set_intro("Please set the value of description", "blue");
// if (frm.is_new()) {
//   frappe.msgprint("welcome to details doctype")
//  }

//     frm.add_custom_button("click me to enjoy",()=>{
//         frappe.msgprint("welcome to")
//     })
//     // frm.remove_custom_button("click me to enjoy")
//     // }
//     frm.change_custom_button_type(
//     "click me to enjoy",
//     null,
//     "primary"
//  )
// frm.set_df_property("name3","reqd",1)
// frm.toggle_enable("status", true);
// frm.toggle_reqd('priority', frm.doc.status === 'Active');
// frm.set_query("first", () => {
//     return {
//         filters: {
//             name1: "preethi"
//         }
//     };
//  }
// });
//  get_email_recipient_filters(frm, field) {

//         return {
//             status: "Active"
//         };

//     }
// }})

// frappe.ui.form.on("details",{

// })

// frappe.ui.form.on("details", {
//     // status_add(frm, cdt, cdn) {
//     //     frappe.msgprint("New item row added");
//     // }
//     refresh(frm)
//     {
//     console.log(frappe.get_route())
//     }   
// });
// frappe.provide("details_app.utils");

// details_app.utils.say_hello = function() {
//     frappe.msgprint("Hello from details app!");
// };

// frappe.ui.form.on("details", {
//     refresh(frm) {

//         frm.add_custom_button("Say Hello", () => {

//             details_app.utils.say_hello();

//         });

//     }
// });
frappe.ui.form.on("details", {
    refresh(frm) {
        if (frappe.user.has_role("Sales User")) {
            frm.set_df_property("name3", "read_only", 1);
        }
    }
});