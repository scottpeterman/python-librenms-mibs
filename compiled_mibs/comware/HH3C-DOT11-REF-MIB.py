# SNMP MIB module (HH3C-DOT11-REF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-DOT11-REF-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:31:06 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hh3cDot11 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75)
)
if mibBuilder.loadTexts:
    hh3cDot11.setRevisions(
        ("2021-01-08 18:00",
         "2016-03-11 18:00",
         "2010-01-07 20:00",
         "2009-05-07 20:00",
         "2007-06-21 20:00",
         "2007-04-27 20:00",
         "2006-05-10 19:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cDot11ObjectIDType(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )



class Hh3cDot11RadioScopeType(TextualConvention, Integer32):
    status = "current"


class Hh3cDot11RadioType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 1),
          ("dot11b", 2),
          ("dot11g", 4),
          ("dot11n", 8),
          ("dot11gn", 16),
          ("dot11an", 32),
          ("dot11ac", 64),
          ("dot11gac", 128),
          ("dot11ax", 256),
          ("dot11gax", 512))
    )



class Hh3cDot11RadioType2(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 1),
          ("dot11b", 2),
          ("dot11g", 4),
          ("dot11an", 8),
          ("dot11gn", 16),
          ("dot11ac", 32),
          ("dot11gac", 64),
          ("dot11ax", 128),
          ("dot11gax", 256))
    )



class Hh3cDot11MACModeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("split", 1),
          ("localtunnel", 2),
          ("localbridge", 3),
          ("fatAP", 4))
    )



class Hh3cDot11ChannelScopeType(TextualConvention, Integer32):
    status = "current"


class Hh3cDot11NotifyReasonType(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class Hh3cDot11SSIDStringType(TextualConvention, OctetString):
    status = "current"


class Hh3cDot11ServicePolicyIDType(TextualConvention, Integer32):
    status = "current"


class Hh3cDot11SSIDEncryptModeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cleartxt", 1),
          ("cipher", 2),
          ("ext", 3))
    )



class Hh3cDot11PreambleType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 1),
          ("short", 2))
    )



class Hh3cDot11TxPwrLevelScopeType(TextualConvention, Integer32):
    status = "current"


class Hh3cDot11RFModeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("auto", 2))
    )



class Hh3cDot11TunnelSecSchemType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cleartxt", 1),
          ("dtls", 2),
          ("ipsec", 3))
    )



class Hh3cDot11SecIEStatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("rsn", 2),
          ("wpa", 3),
          ("all", 4),
          ("ext", 5))
    )



class Hh3cDot11CipherType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              16,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("wep40", 2),
          ("tkip", 4),
          ("aesccmp", 16),
          ("wep104", 32),
          ("wpisms4", 64),
          ("wep128", 128))
    )



class Hh3cDot11AuthenType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("opensystem", 2),
          ("sharedkey", 3),
          ("all", 4))
    )



class Hh3cDot11AKMType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("psk", 2),
          ("dot1x", 3),
          ("ext", 4))
    )



class Hh3cDot11AssocFailType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknownfailure", 1),
          ("toomanyassoc", 2),
          ("invalidie", 3),
          ("unsupportedrate", 4),
          ("unsupportedpwrcap", 5),
          ("unsupportedcap", 6))
    )



class Hh3cDot11AuthorFailType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknownfailure", 1),
          ("invalidie", 2),
          ("rsnieversionunsupported", 3),
          ("wpaieversionunsupported", 4),
          ("groupcipherinvalid", 5),
          ("pairwisecipherinvalid", 6),
          ("akminvalid", 7))
    )



class Hh3cDot11QosAcType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("acbk", 1),
          ("acbe", 2),
          ("acvi", 3),
          ("acvo", 4))
    )



class Hh3cDot11RadioElementIndex(TextualConvention, Unsigned32):
    status = "current"


class Hh3cDot11WorkMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("monitor", 2),
          ("hybrid", 3))
    )



class Hh3cDot11CirMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )



class Hh3cDot11SaIntfDevType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("microwave", 1),
          ("microwaveInverter", 2),
          ("bluetooth", 3),
          ("fixedFreqOthers", 4),
          ("fixedFreqCordlessPhone", 5),
          ("fixedFreqVideo", 6),
          ("fixedFreqAudio", 7),
          ("freqHopperOthers", 8),
          ("freqHopperCordlessBase", 9),
          ("freqHopperCordlessNetwork", 10),
          ("freqHopperXbox", 11),
          ("genericInterferer", 12))
    )



class Hh3cDot11TruthValueCM(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dot11false", 0),
          ("dot11true", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cDot11Common_ObjectIdentity = ObjectIdentity
hh3cDot11Common = _Hh3cDot11Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 12)
)
_Hh3cDot11ElementGroup_ObjectIdentity = ObjectIdentity
hh3cDot11ElementGroup = _Hh3cDot11ElementGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1)
)
_Hh3cDot11APElementTable_Object = MibTable
hh3cDot11APElementTable = _Hh3cDot11APElementTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11APElementTable.setStatus("current")
_Hh3cDot11APElementEntry_Object = MibTableRow
hh3cDot11APElementEntry = _Hh3cDot11APElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 1, 1)
)
hh3cDot11APElementEntry.setIndexNames(
    (0, "HH3C-DOT11-REF-MIB", "hh3cDot11APElementIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11APElementEntry.setStatus("current")
_Hh3cDot11APElementIndex_Type = Integer32
_Hh3cDot11APElementIndex_Object = MibTableColumn
hh3cDot11APElementIndex = _Hh3cDot11APElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 1, 1, 1),
    _Hh3cDot11APElementIndex_Type()
)
hh3cDot11APElementIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11APElementIndex.setStatus("current")
_Hh3cDot11APElementTemplateName_Type = OctetString
_Hh3cDot11APElementTemplateName_Object = MibTableColumn
hh3cDot11APElementTemplateName = _Hh3cDot11APElementTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 1, 1, 2),
    _Hh3cDot11APElementTemplateName_Type()
)
hh3cDot11APElementTemplateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APElementTemplateName.setStatus("current")
_Hh3cDot11APElementSerialID_Type = OctetString
_Hh3cDot11APElementSerialID_Object = MibTableColumn
hh3cDot11APElementSerialID = _Hh3cDot11APElementSerialID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 1, 1, 3),
    _Hh3cDot11APElementSerialID_Type()
)
hh3cDot11APElementSerialID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APElementSerialID.setStatus("current")
_Hh3cDot11APElementModelAlias_Type = OctetString
_Hh3cDot11APElementModelAlias_Object = MibTableColumn
hh3cDot11APElementModelAlias = _Hh3cDot11APElementModelAlias_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 1, 1, 4),
    _Hh3cDot11APElementModelAlias_Type()
)
hh3cDot11APElementModelAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APElementModelAlias.setStatus("current")
_Hh3cDot11RadioElementTable_Object = MibTable
hh3cDot11RadioElementTable = _Hh3cDot11RadioElementTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11RadioElementTable.setStatus("current")
_Hh3cDot11RadioElementEntry_Object = MibTableRow
hh3cDot11RadioElementEntry = _Hh3cDot11RadioElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 2, 1)
)
hh3cDot11RadioElementEntry.setIndexNames(
    (0, "HH3C-DOT11-REF-MIB", "hh3cDot11APElementIndex"),
    (0, "HH3C-DOT11-REF-MIB", "hh3cDot11RadioElementRadioNum"),
)
if mibBuilder.loadTexts:
    hh3cDot11RadioElementEntry.setStatus("current")
_Hh3cDot11RadioElementRadioNum_Type = Unsigned32
_Hh3cDot11RadioElementRadioNum_Object = MibTableColumn
hh3cDot11RadioElementRadioNum = _Hh3cDot11RadioElementRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 2, 1, 1),
    _Hh3cDot11RadioElementRadioNum_Type()
)
hh3cDot11RadioElementRadioNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RadioElementRadioNum.setStatus("current")
_Hh3cDot11RadioElementRadioPolicy_Type = OctetString
_Hh3cDot11RadioElementRadioPolicy_Object = MibTableColumn
hh3cDot11RadioElementRadioPolicy = _Hh3cDot11RadioElementRadioPolicy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 2, 1, 2),
    _Hh3cDot11RadioElementRadioPolicy_Type()
)
hh3cDot11RadioElementRadioPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioElementRadioPolicy.setStatus("current")
_Hh3cDot11RadioElementRadioIndex_Type = Unsigned32
_Hh3cDot11RadioElementRadioIndex_Object = MibTableColumn
hh3cDot11RadioElementRadioIndex = _Hh3cDot11RadioElementRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 2, 1, 3),
    _Hh3cDot11RadioElementRadioIndex_Type()
)
hh3cDot11RadioElementRadioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RadioElementRadioIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DOT11-REF-MIB",
    **{"Hh3cDot11ObjectIDType": Hh3cDot11ObjectIDType,
       "Hh3cDot11RadioScopeType": Hh3cDot11RadioScopeType,
       "Hh3cDot11RadioType": Hh3cDot11RadioType,
       "Hh3cDot11RadioType2": Hh3cDot11RadioType2,
       "Hh3cDot11MACModeType": Hh3cDot11MACModeType,
       "Hh3cDot11ChannelScopeType": Hh3cDot11ChannelScopeType,
       "Hh3cDot11NotifyReasonType": Hh3cDot11NotifyReasonType,
       "Hh3cDot11SSIDStringType": Hh3cDot11SSIDStringType,
       "Hh3cDot11ServicePolicyIDType": Hh3cDot11ServicePolicyIDType,
       "Hh3cDot11SSIDEncryptModeType": Hh3cDot11SSIDEncryptModeType,
       "Hh3cDot11PreambleType": Hh3cDot11PreambleType,
       "Hh3cDot11TxPwrLevelScopeType": Hh3cDot11TxPwrLevelScopeType,
       "Hh3cDot11RFModeType": Hh3cDot11RFModeType,
       "Hh3cDot11TunnelSecSchemType": Hh3cDot11TunnelSecSchemType,
       "Hh3cDot11SecIEStatusType": Hh3cDot11SecIEStatusType,
       "Hh3cDot11CipherType": Hh3cDot11CipherType,
       "Hh3cDot11AuthenType": Hh3cDot11AuthenType,
       "Hh3cDot11AKMType": Hh3cDot11AKMType,
       "Hh3cDot11AssocFailType": Hh3cDot11AssocFailType,
       "Hh3cDot11AuthorFailType": Hh3cDot11AuthorFailType,
       "Hh3cDot11QosAcType": Hh3cDot11QosAcType,
       "Hh3cDot11RadioElementIndex": Hh3cDot11RadioElementIndex,
       "Hh3cDot11WorkMode": Hh3cDot11WorkMode,
       "Hh3cDot11CirMode": Hh3cDot11CirMode,
       "Hh3cDot11SaIntfDevType": Hh3cDot11SaIntfDevType,
       "Hh3cDot11TruthValueCM": Hh3cDot11TruthValueCM,
       "hh3cDot11": hh3cDot11,
       "hh3cDot11Common": hh3cDot11Common,
       "hh3cDot11ElementGroup": hh3cDot11ElementGroup,
       "hh3cDot11APElementTable": hh3cDot11APElementTable,
       "hh3cDot11APElementEntry": hh3cDot11APElementEntry,
       "hh3cDot11APElementIndex": hh3cDot11APElementIndex,
       "hh3cDot11APElementTemplateName": hh3cDot11APElementTemplateName,
       "hh3cDot11APElementSerialID": hh3cDot11APElementSerialID,
       "hh3cDot11APElementModelAlias": hh3cDot11APElementModelAlias,
       "hh3cDot11RadioElementTable": hh3cDot11RadioElementTable,
       "hh3cDot11RadioElementEntry": hh3cDot11RadioElementEntry,
       "hh3cDot11RadioElementRadioNum": hh3cDot11RadioElementRadioNum,
       "hh3cDot11RadioElementRadioPolicy": hh3cDot11RadioElementRadioPolicy,
       "hh3cDot11RadioElementRadioIndex": hh3cDot11RadioElementRadioIndex}
)
