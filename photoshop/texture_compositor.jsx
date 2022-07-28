
function create_color_document(){
    /*
    カラーテクスチャ用のRGBドキュメント
    */

    var idmake = stringIDToTypeID( "make" );
    var desc5 = new ActionDescriptor();
    var idnew = stringIDToTypeID( "new" );
    var desc6 = new ActionDescriptor();
    var idartboard = stringIDToTypeID( "artboard" );

    desc6.putBoolean( idartboard, false );
    var idautoPromoteBackgroundLayer = stringIDToTypeID( "autoPromoteBackgroundLayer" );
    desc6.putBoolean( idautoPromoteBackgroundLayer, false );
    var idmode = stringIDToTypeID( "mode" );
    var idRGBColorMode = stringIDToTypeID( "RGBColorMode" );
    desc6.putClass( idmode, idRGBColorMode );
    var idwidth = stringIDToTypeID( "width" );
    var iddistanceUnit = stringIDToTypeID( "distanceUnit" );
    desc6.putUnitDouble( idwidth, iddistanceUnit, 2048.000000 );
    var idheight = stringIDToTypeID( "height" );
    var iddistanceUnit = stringIDToTypeID( "distanceUnit" );
    desc6.putUnitDouble( idheight, iddistanceUnit, 2048.000000 );
    var idresolution = stringIDToTypeID( "resolution" );
    var iddensityUnit = stringIDToTypeID( "densityUnit" );
    desc6.putUnitDouble( idresolution, iddensityUnit, 72.000000 );
    var idpixelScaleFactor = stringIDToTypeID( "pixelScaleFactor" );
    desc6.putDouble( idpixelScaleFactor, 1.000000 );
    var idfill = stringIDToTypeID( "fill" );
    var idtransparency = stringIDToTypeID( "transparency" );
    desc6.putEnumerated( idfill, idfill, idtransparency );
    var iddepth = stringIDToTypeID( "depth" );
    desc6.putInteger( iddepth, 8 );
    var idprofile = stringIDToTypeID( "profile" );
    desc6.putString( idprofile, """sRGB IEC61966-2.1""" );
    var idguides = stringIDToTypeID( "guides" );
    var list2 = new ActionList();
    desc6.putList( idguides, list2 );
    var iddocument = stringIDToTypeID( "document" );
    desc5.putObject( idnew, iddocument, desc6 );

    executeAction( idmake, desc5, DialogModes.NO );
}

function create_gray_document(){
    /*
    質感設定用グレーのドキュメント
    */

    var idmake = stringIDToTypeID( "make" );
    var desc5 = new ActionDescriptor();
    var idnew = stringIDToTypeID( "new" );
    var desc6 = new ActionDescriptor();
    var idartboard = stringIDToTypeID( "artboard" );

    desc6.putBoolean( idartboard, false );
    var idautoPromoteBackgroundLayer = stringIDToTypeID( "autoPromoteBackgroundLayer" );
    desc6.putBoolean( idautoPromoteBackgroundLayer, false );
    var idmode = stringIDToTypeID( "mode" );
    var idRGBColorMode = stringIDToTypeID( "grayscaleMode" );
    desc6.putClass( idmode, idRGBColorMode );
    var idwidth = stringIDToTypeID( "width" );
    var iddistanceUnit = stringIDToTypeID( "distanceUnit" );
    desc6.putUnitDouble( idwidth, iddistanceUnit, 2048.000000 );
    var idheight = stringIDToTypeID( "height" );
    var iddistanceUnit = stringIDToTypeID( "distanceUnit" );
    desc6.putUnitDouble( idheight, iddistanceUnit, 2048.000000 );
    var idresolution = stringIDToTypeID( "resolution" );
    var iddensityUnit = stringIDToTypeID( "densityUnit" );
    desc6.putUnitDouble( idresolution, iddensityUnit, 72.000000 );
    var idpixelScaleFactor = stringIDToTypeID( "pixelScaleFactor" );
    desc6.putDouble( idpixelScaleFactor, 1.000000 );
    var idfill = stringIDToTypeID( "fill" );
    var idtransparency = stringIDToTypeID( "transparency" );
    desc6.putEnumerated( idfill, idfill, idtransparency );
    var iddepth = stringIDToTypeID( "depth" );
    desc6.putInteger( iddepth, 8 );
    var idprofile = stringIDToTypeID( "profile" );
    desc6.putString( idprofile, """sGray""" );
    var idguides = stringIDToTypeID( "guides" );
    var list2 = new ActionList();
    desc6.putList( idguides, list2 );
    var iddocument = stringIDToTypeID( "document" );
    desc5.putObject( idnew, iddocument, desc6 );

    executeAction( idmake, desc5, DialogModes.NO );

}

function create_export_folder(textureset_folder){
    /*
    エクスポート先を作成
    */

    var f = new Folder (textureset_folder + "/export");
    f.create();
}

function get_folder_path(){
    /*
    ダイアログからパスを取得
    パスを返却
    */

    var p = Folder.selectDialog('TextureSetフォルダを選択');

    if (p == null) {
        return null
    }
    else{
        return p
    }
}

function get_textures(folder_path, suffix_length, suffix){
    /*
    対象となるテクスチャを全て取得
    テクスチャのパスリストを返却
    */

    // フォルダパスからテクスチャを全て取得
    var textures = folder_path.getFiles();

    var textures_list = []
    for(var i=0; i<textures.length; i++){
        var name = String(textures[i]);
        if ( name.slice(-suffix_length) == suffix+".tga" ){
            textures_list.push(decodeURI(textures[i]));//日本語にも対応するようにデコード
        }
    }

    return textures_list
}

function import_texture(path){
    /*
    渡されたパスからテクスチャをインポート
    */

    var idplaceEvent = stringIDToTypeID( "placeEvent" );
    var desc8 = new ActionDescriptor();
    var idID = stringIDToTypeID( "ID" );
    desc8.putInteger( idID, 3 );
    var idnull = stringIDToTypeID( "null" );
    desc8.putPath( idnull, new File( path ) );
    var idfreeTransformCenterState = stringIDToTypeID( "freeTransformCenterState" );
    var idquadCenterState = stringIDToTypeID( "quadCenterState" );
    var idQCSAverage = stringIDToTypeID( "QCSAverage" );
    desc8.putEnumerated( idfreeTransformCenterState, idquadCenterState, idQCSAverage );

    var idoffset = stringIDToTypeID( "offset" );
    var desc9 = new ActionDescriptor();
    var idhorizontal = stringIDToTypeID( "horizontal" );
    var idpixelsUnit = stringIDToTypeID( "pixelsUnit" );
    desc9.putUnitDouble( idhorizontal, idpixelsUnit, 0.000000 );

    var idvertical = stringIDToTypeID( "vertical" );
    var idpixelsUnit = stringIDToTypeID( "pixelsUnit" );
    desc9.putUnitDouble( idvertical, idpixelsUnit, 0.000000 );

    var idoffset = stringIDToTypeID( "offset" );
    desc8.putObject( idoffset, idoffset, desc9 );

    executeAction( idplaceEvent, desc8, DialogModes.NO );
}

function select_layer(layer_name){
    /*
    パスからレイヤーを作成して選択
    */

    var n = layer_name.replace("\\", "/");
    n = n.split("/");
    n = String(n.slice(-1));
    n = n.slice(0, -4);

    var idselect = stringIDToTypeID( "select" );
    var desc222 = new ActionDescriptor();
    var idnull = stringIDToTypeID( "null" );
    var ref16 = new ActionReference();
    var idlayer = stringIDToTypeID( "layer" );
    ref16.putName( idlayer, n );
    desc222.putReference( idnull, ref16 );

    executeAction( idselect, desc222, DialogModes.NO );
}

function set_layer_mode(mode){
    /*
    レイヤーモードを比較（明）に変換
    */

    var idset = stringIDToTypeID( "set" );
    var desc323 = new ActionDescriptor();
    var idnull = stringIDToTypeID( "null" );
    var ref47 = new ActionReference();
    var idlayer = stringIDToTypeID( "layer" );
    var idordinal = stringIDToTypeID( "ordinal" );
    var idtargetEnum = stringIDToTypeID( "targetEnum" );
    ref47.putEnumerated( idlayer, idordinal, idtargetEnum );
    desc323.putReference( idnull, ref47 );

    var idto = stringIDToTypeID( "to" );
    var desc324 = new ActionDescriptor();
    var idmode = stringIDToTypeID( "mode" );
    var idblendMode = stringIDToTypeID( "blendMode" );
    var idlighten = stringIDToTypeID( mode );
    desc324.putEnumerated( idmode, idblendMode, idlighten );

    var idlayer = stringIDToTypeID( "layer" );
    desc323.putObject( idto, idlayer, desc324 );

    executeAction( idset, desc323, DialogModes.NO );
}

function export_texture(folder_path, true_name, texture_type){
    /*
    テクスチャを書き出し
    */

    var export_path = folder_path + "/export/" + true_name + texture_type + ".tga";

    var idsave = stringIDToTypeID( "save" );
    var desc204 = new ActionDescriptor();
    var idas = stringIDToTypeID( "as" );
    var desc205 = new ActionDescriptor();
    var idbitDepth = stringIDToTypeID( "bitDepth" );
    desc205.putInteger( idbitDepth, 16 );
    var idcompression = stringIDToTypeID( "compression" );
    desc205.putInteger( idcompression, 0 );

    var idtargaFormat = stringIDToTypeID( "targaFormat" );
    desc204.putObject( idas, idtargaFormat, desc205 );
    var idin = stringIDToTypeID( "in" );
    desc204.putPath( idin, new File(export_path) );
    var iddocumentID = stringIDToTypeID( "documentID" );
    desc204.putInteger( iddocumentID, 228 );
    var idcopy = stringIDToTypeID( "copy" );
    desc204.putBoolean( idcopy, true );
    var idlowerCase = stringIDToTypeID( "lowerCase" );
    desc204.putBoolean( idlowerCase, true );

    var idsaveStage = stringIDToTypeID( "saveStage" );
    var idsaveStageType = stringIDToTypeID( "saveStageType" );
    var idsaveBegin = stringIDToTypeID( "saveBegin" );
    desc204.putEnumerated( idsaveStage, idsaveStageType, idsaveBegin );
    executeAction( idsave, desc204, DialogModes.NO );
}

function close_document(){
    /*
    ドキュメントを閉じる
    */

    var idclose = stringIDToTypeID( "close" );
    var desc396 = new ActionDescriptor();
    var idsaving = stringIDToTypeID( "saving" );
    var idyesNo = stringIDToTypeID( "yesNo" );
    var idno = stringIDToTypeID( "no" );

    desc396.putEnumerated( idsaving, idyesNo, idno );
    var iddocumentID = stringIDToTypeID( "documentID" );
    desc396.putInteger( iddocumentID, 834 );
    var idforceNotify = stringIDToTypeID( "forceNotify" );
    desc396.putBoolean( idforceNotify, true );

    executeAction( idclose, desc396, DialogModes.NO );
}

/*
function rename_temp_rgb(){
    return
}

function create_new_channel(){
    var idset = stringIDToTypeID( "set" );
    var desc464 = new ActionDescriptor();
    var idnull = stringIDToTypeID( "null" );
    var ref142 = new ActionReference();
    var idchannel = stringIDToTypeID( "channel" );
    var idselection = stringIDToTypeID( "selection" );
    ref142.putProperty( idchannel, idselection );
    desc464.putReference( idnull, ref142 );
    var idto = stringIDToTypeID( "to" );
    var ref143 = new ActionReference();
    var idchannel = stringIDToTypeID( "channel" );
    var idchannel = stringIDToTypeID( "channel" );
    var idRGB = stringIDToTypeID( "RGB" );
    ref143.putEnumerated( idchannel, idchannel, idRGB );
    desc464.putReference( idto, ref143 );
    executeAction( idset, desc464, DialogModes.NO );

    var idduplicate = stringIDToTypeID( "duplicate" );
    var desc411 = new ActionDescriptor();
    var idnull = stringIDToTypeID( "null" );
    var ref113 = new ActionReference();
    var idchannel = stringIDToTypeID( "channel" );
    var idselection = stringIDToTypeID( "selection" );
    ref113.putProperty( idchannel, idselection );
    desc411.putReference( idnull, ref113 );
    executeAction( idduplicate, desc411, DialogModes.NO );

    var idselect = stringIDToTypeID( "select" );
    var desc423 = new ActionDescriptor();
    var idnull = stringIDToTypeID( "null" );
    var ref121 = new ActionReference();
    var idchannel = stringIDToTypeID( "channel" );
    ref121.putName( idchannel, "Alpha 1" );
    desc423.putReference( idnull, ref121 );
    executeAction( idselect, desc423, DialogModes.NO );

    var idset = stringIDToTypeID( "set" );
    var desc475 = new ActionDescriptor();
    var idnull = stringIDToTypeID( "null" );
    var ref148 = new ActionReference();
    var idchannel = stringIDToTypeID( "channel" );
    var idordinal = stringIDToTypeID( "ordinal" );
    var idtargetEnum = stringIDToTypeID( "targetEnum" );
    ref148.putEnumerated( idchannel, idordinal, idtargetEnum );
    desc475.putReference( idnull, ref148 );
    var idto = stringIDToTypeID( "to" );
    var desc476 = new ActionDescriptor();
    var idname = stringIDToTypeID( "name" );
    desc476.putString( idname, """Red""" );
    var idchannel = stringIDToTypeID( "channel" );
    desc475.putObject( idto, idchannel, desc476 );
    executeAction( idset, desc475, DialogModes.NO );
}
*/

function combine_painter_texture(folder_path, true_name, raw_texture_list, type){
    /*
    テクスチャを結合
    */

    // 作業用のドキュメントを作成
    if (type == "Metallic"  ||
        type == "Roughness" ||
        type == "AO"        ||
        type == "Opacity"){
        create_gray_document();
    }else{
        create_color_document();
    }

    // テクスチャを一つづつ処理する
    for(var i=0; i<raw_texture_list.length; i++){
        import_texture(raw_texture_list[i]);

        // 最下層のレイヤーでなければレイヤーの合成モードを変更
        if (i != 0){
            select_layer(raw_texture_list[i]);
            if(type == "Nornal"){
                set_layer_mode("overlay"); // Normalなら合成モードをOverLayに
            }else{
                set_layer_mode("lighten");
            }
        }
    }
    // テクスチャを書き出し
    export_texture(folder_path, true_name, type);

    close_document();
}

function conbine_ccc_texture(folder_path, true_name){
    // create_color_document();
    import_texture(folder_path + "/export/" + true_name + "Roughness.tga");

    create_new_channel();
}


function main(){
    // テクスチャの格納されているフォルダを取得
    var folder_path = get_folder_path();

    // エクスポート先のフォルダを作成
    create_export_folder(folder_path);

    // フォルダパスからテクスチャを全て取得
    var basecolor_list = get_textures(folder_path, 13, "BaseColor");　// 拡張子分＋4
    var metallic_list = get_textures(folder_path, 12, "Metallic");
    var roughness_list = get_textures(folder_path, 13, "Roughness");
    var ao_list = get_textures(folder_path, 6, "AO");
    var emissive_list = get_textures(folder_path, 12, "Emissive");
    var opacity_list = get_textures(folder_path, 11, "Opacity");
    var normal_list = get_textures(folder_path, 10, "Normal");

    // 純粋なアセットの名前を取得 ex.)2000Mill
    var true_name = basecolor_list[0];
    true_name = true_name.replace("\\", "/");
    true_name = true_name.split("/");
    true_name = String(true_name.slice(-1));
    true_name = true_name.slice(0, -4);
    true_name = true_name.split("_");
    true_name = String(true_name[0]);

    // テクスチャ結合処理を開始
    if (basecolor_list.length != 0){
        combine_painter_texture(folder_path, true_name, basecolor_list, "BaseColor");
    }
    if (metallic_list.length != 0){
        combine_painter_texture(folder_path, true_name, metallic_list, "Metallic");
    }
    if (roughness_list.length != 0){
        combine_painter_texture(folder_path, true_name, roughness_list, "Roughness");
    }
    if (ao_list.length != 0){
        combine_painter_texture(folder_path, true_name, ao_list, "AO");
    }
    if (emissive_list.length != 0){
        combine_painter_texture(folder_path, true_name, emissive_list, "Emissive");
    }
    if (opacity_list.length != 0){
        combine_painter_texture(folder_path, true_name, opacity_list, "Opacity");
    }
    if (normal_list.length != 0){
        combine_painter_texture(folder_path, true_name, normal_list, "Normal");
    }

    alert("書き出しが完了しました。");

    // conbine_ccc_texture(folder_path, true_name);

}
main();
