
function create_color_document(){
    /*
    カラーテクスチャ用のRGBドキュメント
    */

    var idmake = stringIDToTypeID( "make" );
    var desc299 = new ActionDescriptor();
    var idnew = stringIDToTypeID( "new" );
    var desc300 = new ActionDescriptor();
    var idartboard = stringIDToTypeID( "artboard" );

    desc300.putBoolean( idartboard, false );
    var idautoPromoteBackgroundLayer = stringIDToTypeID( "autoPromoteBackgroundLayer" );
    desc300.putBoolean( idautoPromoteBackgroundLayer, false );
    var idmode = stringIDToTypeID( "mode" );
    var idRGBColorMode = stringIDToTypeID( "RGBColorMode" );
    desc300.putClass( idmode, idRGBColorMode );
    var idwidth = stringIDToTypeID( "width" );
    var iddistanceUnit = stringIDToTypeID( "distanceUnit" );
    desc300.putUnitDouble( idwidth, iddistanceUnit, 491.520000 );
    var idheight = stringIDToTypeID( "height" );
    var iddistanceUnit = stringIDToTypeID( "distanceUnit" );
    desc300.putUnitDouble( idheight, iddistanceUnit, 491.520000 );
    var idresolution = stringIDToTypeID( "resolution" );
    var iddensityUnit = stringIDToTypeID( "densityUnit" );
    desc300.putUnitDouble( idresolution, iddensityUnit, 300.000000 );
    var idpixelScaleFactor = stringIDToTypeID( "pixelScaleFactor" );
    desc300.putDouble( idpixelScaleFactor, 1.000000 );
    var idfill = stringIDToTypeID( "fill" );
    var idfill = stringIDToTypeID( "fill" );
    var idtransparency = stringIDToTypeID( "transparency" );
    desc300.putEnumerated( idfill, idfill, idtransparency );
    var iddepth = stringIDToTypeID( "depth" );
    desc300.putInteger( iddepth, 8 );
    var idprofile = stringIDToTypeID( "profile" );
    desc300.putString( idprofile, """sRGB IEC61966-2.1""" );
    var idguides = stringIDToTypeID( "guides" );
    var list39 = new ActionList();
    desc300.putList( idguides, list39 );

    var iddocument = stringIDToTypeID( "document" );
    desc299.putObject( idnew, iddocument, desc300 );
    var iddocumentID = stringIDToTypeID( "documentID" );
    desc299.putInteger( iddocumentID, 324 );

    executeAction( idmake, desc299, DialogModes.NO );
}

function create_gray_document(){
    /*
    質感設定用グレーのドキュメント
    */

    var idmake = stringIDToTypeID( "make" );
    var desc415 = new ActionDescriptor();
    var idnew = stringIDToTypeID( "new" );
    var desc416 = new ActionDescriptor();
    var idartboard = stringIDToTypeID( "artboard" );

    desc416.putBoolean( idartboard, false );
    var idautoPromoteBackgroundLayer = stringIDToTypeID( "autoPromoteBackgroundLayer" );
    desc416.putBoolean( idautoPromoteBackgroundLayer, false );
    var idmode = stringIDToTypeID( "mode" );
    var idgrayscaleMode = stringIDToTypeID( "grayscaleMode" );
    desc416.putClass( idmode, idgrayscaleMode );
    var idwidth = stringIDToTypeID( "width" );
    var iddistanceUnit = stringIDToTypeID( "distanceUnit" );
    desc416.putUnitDouble( idwidth, iddistanceUnit, 491.520000 );
    var idheight = stringIDToTypeID( "height" );
    var iddistanceUnit = stringIDToTypeID( "distanceUnit" );
    desc416.putUnitDouble( idheight, iddistanceUnit, 491.520000 );
    var idresolution = stringIDToTypeID( "resolution" );
    var iddensityUnit = stringIDToTypeID( "densityUnit" );
    desc416.putUnitDouble( idresolution, iddensityUnit, 300.000000 );
    var idpixelScaleFactor = stringIDToTypeID( "pixelScaleFactor" );
    desc416.putDouble( idpixelScaleFactor, 1.000000 );
    var idfill = stringIDToTypeID( "fill" );
    var idfill = stringIDToTypeID( "fill" );
    var idtransparency = stringIDToTypeID( "transparency" );
    desc416.putEnumerated( idfill, idfill, idtransparency );
    var iddepth = stringIDToTypeID( "depth" );
    desc416.putInteger( iddepth, 8 );
    var idprofile = stringIDToTypeID( "profile" );
    desc416.putString( idprofile, """Dot Gain 20%""" );
    var idguides = stringIDToTypeID( "guides" );
    var list58 = new ActionList();
    desc416.putList( idguides, list58 );

    var iddocument = stringIDToTypeID( "document" );
    desc415.putObject( idnew, iddocument, desc416 );
    var iddocumentID = stringIDToTypeID( "documentID" );
    desc415.putInteger( iddocumentID, 2050 );

    executeAction( idmake, desc415, DialogModes.NO );

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

function main(){

    // テクスチャの格納されているフォルダを取得
    var folder_path = get_folder_path();

    // エクスポート先のフォルダを作成
    create_export_folder(folder_path);

    // フォルダパスからテクスチャを全て取得
    var basecolor_list = get_textures(folder_path, 13, "BaseColor");
    var metallic_list = get_textures(folder_path, 12, "Metallic");
    var roughness_list = get_textures(folder_path, 13, "Roughness");
    var ao_list = get_textures(folder_path, 13, "AO");
    var emissive_list = get_textures(folder_path, 13, "Emissive");
    var opacity_list = get_textures(folder_path, 13, "Opacity");
    var normal_list = get_textures(folder_path, 10, "Normal");

    // 純粋なアセットの名前を取得 ex.)2000Mill
    var true_name = basecolor_list[0];
    true_name = true_name.replace("\\", "/");
    true_name = true_name.split("/");
    true_name = String(true_name.slice(-1));
    true_name = true_name.slice(0, -4);
    true_name = true_name.split("_");
    true_name = String(true_name[0]);

    // 作業用のドキュメントを作成
    create_color_document();
    // テクスチャを一つづつ処理する
    for(var i=0; i<basecolor_list.length; i++){
        import_texture(basecolor_list[i]);

        // 最下層のレイヤーでなければレイヤーの合成モードを変更
        if (i != 0){
            select_layer(basecolor_list[i]);
            set_layer_mode("lighten");
        }
    }
    // ベースカラーのテクスチャを書き出し
    if ( basecolor_list.length != 0 ){
        export_texture(folder_path, true_name, "BaseColor");
    }
    close_document();

    // metallic
    create_gray_document();
    for(var i=0; i<metallic_list.length; i++){
        import_texture(metallic_list[i]);
        if (i != 0){
            select_layer(metallic_list[i]);
            set_layer_mode("lighten");
        }
    }
    if ( metallic_list.length != 0 ){
        export_texture(folder_path, true_name, "Metallic");
    }
    close_document();

    // roughness
    create_gray_document();
    for(var i=0; i<roughness_list.length; i++){
        import_texture(roughness_list[i]);
        if (i != 0){
            select_layer(roughness_list[i]);
            set_layer_mode("lighten");
        }
    }
    if ( roughness_list.length != 0 ){
        export_texture(folder_path, true_name, "Roughness");
    }
    close_document();

    // AO
    create_gray_document();
    for(var i=0; i<ao_list.length; i++){
        import_texture(ao_list[i]);
        if (i != 0){
            select_layer(ao_list[i]);
            set_layer_mode("lighten");
        }
    }
    if ( ao_list.length != 0 ){
        export_texture(folder_path, true_name, "AO");
    }
    close_document();

    // Emissive
    create_color_document();
    for(var i=0; i<emissive_list.length; i++){
        import_texture(emissive_list[i]);
        if (i != 0){
            select_layer(emissive_list[i]);
            set_layer_mode("lighten");
        }
    }
    if ( emissive_list.length != 0 ){
        export_texture(folder_path, true_name, "Emissive");
    }
    close_document();

    // Opacity
    create_gray_document();
    for(var i=0; i<opacity_list.length; i++){
        import_texture(opacity_list[i]);
        if (i != 0){
            select_layer(opacity_list[i]);
            set_layer_mode("lighten");
        }
    }
    if ( opacity_list.length != 0 ){
        export_texture(folder_path, true_name, "Opacity");
    }
    close_document();

    // Normal
    create_color_document();
    for(var i=0; i<normal_list.length; i++){
        import_texture(normal_list[i]);
        if (i != 0){
            select_layer(normal_list[i]);
            set_layer_mode("overlay");
        }
    }
    if ( normal_list.length != 0 ){
        export_texture(folder_path, true_name, "Opacity");
    }
    close_document();

    alert("書き出しが完了しました。");
}
main();
