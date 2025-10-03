# SNMP MIB module (NMS-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bdcom\NMS-IF-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:45:33 2025
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

(nmsMgmt,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmsMgmt")

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

nmsIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NmsIfObjects_ObjectIdentity = ObjectIdentity
nmsIfObjects = _NmsIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1)
)
_VifTable_Object = MibTable
vifTable = _VifTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 1)
)
if mibBuilder.loadTexts:
    vifTable.setStatus("mandatory")
_VifEntry_Object = MibTableRow
vifEntry = _VifEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 1, 1)
)
vifEntry.setIndexNames(
    (0, "NMS-IF-MIB", "vifIndex"),
)
if mibBuilder.loadTexts:
    vifEntry.setStatus("mandatory")
_VifIndex_Type = Integer32
_VifIndex_Object = MibTableColumn
vifIndex = _VifIndex_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 1, 1, 1),
    _VifIndex_Type()
)
vifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifIndex.setStatus("mandatory")


class _VifDescr_Type(DisplayString):
    """Custom type vifDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VifDescr_Type.__name__ = "DisplayString"
_VifDescr_Object = MibTableColumn
vifDescr = _VifDescr_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 1, 1, 2),
    _VifDescr_Type()
)
vifDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifDescr.setStatus("mandatory")


class _VifType_Type(Integer32):
    """Custom type vifType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              100,
              101,
              102)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("voiceEM", 100),
          ("voiceFXO", 101),
          ("voiceFXS", 102))
    )


_VifType_Type.__name__ = "Integer32"
_VifType_Object = MibTableColumn
vifType = _VifType_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 1, 1, 3),
    _VifType_Type()
)
vifType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifType.setStatus("mandatory")
_VifMtu_Type = Integer32
_VifMtu_Object = MibTableColumn
vifMtu = _VifMtu_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 1, 1, 4),
    _VifMtu_Type()
)
vifMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifMtu.setStatus("mandatory")
_VifSpeed_Type = Gauge32
_VifSpeed_Object = MibTableColumn
vifSpeed = _VifSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 1, 1, 5),
    _VifSpeed_Type()
)
vifSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifSpeed.setStatus("mandatory")
_VifPhysAddress_Type = PhysAddress
_VifPhysAddress_Object = MibTableColumn
vifPhysAddress = _VifPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 1, 1, 6),
    _VifPhysAddress_Type()
)
vifPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifPhysAddress.setStatus("mandatory")


class _VifAdminStatus_Type(Integer32):
    """Custom type vifAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_VifAdminStatus_Type.__name__ = "Integer32"
_VifAdminStatus_Object = MibTableColumn
vifAdminStatus = _VifAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 1, 1, 7),
    _VifAdminStatus_Type()
)
vifAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vifAdminStatus.setStatus("mandatory")


class _VifOperStatus_Type(Integer32):
    """Custom type vifOperStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("dormant", 5))
    )


_VifOperStatus_Type.__name__ = "Integer32"
_VifOperStatus_Object = MibTableColumn
vifOperStatus = _VifOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 1, 1, 8),
    _VifOperStatus_Type()
)
vifOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifOperStatus.setStatus("mandatory")
_VifLastChange_Type = TimeTicks
_VifLastChange_Object = MibTableColumn
vifLastChange = _VifLastChange_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 1, 1, 9),
    _VifLastChange_Type()
)
vifLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifLastChange.setStatus("mandatory")
_IfStormControlTable_Object = MibTable
ifStormControlTable = _IfStormControlTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 2)
)
if mibBuilder.loadTexts:
    ifStormControlTable.setStatus("mandatory")
_IfStormControlEntry_Object = MibTableRow
ifStormControlEntry = _IfStormControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 2, 1)
)
ifStormControlEntry.setIndexNames(
    (0, "NMS-IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ifStormControlEntry.setStatus("mandatory")
_IfIndex_Type = Integer32
_IfIndex_Object = MibTableColumn
ifIndex = _IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 2, 1, 1),
    _IfIndex_Type()
)
ifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIndex.setStatus("mandatory")


class _IfStormControlBroadcast_Type(Integer32):
    """Custom type ifStormControlBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_IfStormControlBroadcast_Type.__name__ = "Integer32"
_IfStormControlBroadcast_Object = MibTableColumn
ifStormControlBroadcast = _IfStormControlBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 2, 1, 2),
    _IfStormControlBroadcast_Type()
)
ifStormControlBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifStormControlBroadcast.setStatus("mandatory")


class _IfStormControlMulticast_Type(Integer32):
    """Custom type ifStormControlMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_IfStormControlMulticast_Type.__name__ = "Integer32"
_IfStormControlMulticast_Object = MibTableColumn
ifStormControlMulticast = _IfStormControlMulticast_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 2, 1, 3),
    _IfStormControlMulticast_Type()
)
ifStormControlMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifStormControlMulticast.setStatus("mandatory")


class _IfStormControlUnicast_Type(Integer32):
    """Custom type ifStormControlUnicast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_IfStormControlUnicast_Type.__name__ = "Integer32"
_IfStormControlUnicast_Object = MibTableColumn
ifStormControlUnicast = _IfStormControlUnicast_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 2, 1, 4),
    _IfStormControlUnicast_Type()
)
ifStormControlUnicast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifStormControlUnicast.setStatus("mandatory")


class _IfStormControlBroadcastAction_Type(Integer32):
    """Custom type ifStormControlBroadcastAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("shutdown", 1),
          ("block", 2),
          ("resume", 3))
    )


_IfStormControlBroadcastAction_Type.__name__ = "Integer32"
_IfStormControlBroadcastAction_Object = MibTableColumn
ifStormControlBroadcastAction = _IfStormControlBroadcastAction_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 2, 1, 5),
    _IfStormControlBroadcastAction_Type()
)
ifStormControlBroadcastAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifStormControlBroadcastAction.setStatus("mandatory")


class _IfStormControlBroadcastAutoResume_Type(Integer32):
    """Custom type ifStormControlBroadcastAutoResume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 36000),
    )


_IfStormControlBroadcastAutoResume_Type.__name__ = "Integer32"
_IfStormControlBroadcastAutoResume_Object = MibTableColumn
ifStormControlBroadcastAutoResume = _IfStormControlBroadcastAutoResume_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 2, 1, 6),
    _IfStormControlBroadcastAutoResume_Type()
)
ifStormControlBroadcastAutoResume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifStormControlBroadcastAutoResume.setStatus("mandatory")


class _IfStormControlMulticastAction_Type(Integer32):
    """Custom type ifStormControlMulticastAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("shutdown", 1),
          ("block", 2),
          ("resume", 3))
    )


_IfStormControlMulticastAction_Type.__name__ = "Integer32"
_IfStormControlMulticastAction_Object = MibTableColumn
ifStormControlMulticastAction = _IfStormControlMulticastAction_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 2, 1, 7),
    _IfStormControlMulticastAction_Type()
)
ifStormControlMulticastAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifStormControlMulticastAction.setStatus("mandatory")


class _IfStormControlMulticastAutoResume_Type(Integer32):
    """Custom type ifStormControlMulticastAutoResume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 36000),
    )


_IfStormControlMulticastAutoResume_Type.__name__ = "Integer32"
_IfStormControlMulticastAutoResume_Object = MibTableColumn
ifStormControlMulticastAutoResume = _IfStormControlMulticastAutoResume_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 2, 1, 8),
    _IfStormControlMulticastAutoResume_Type()
)
ifStormControlMulticastAutoResume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifStormControlMulticastAutoResume.setStatus("mandatory")


class _IfStormControlMode_Type(Integer32):
    """Custom type ifStormControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pps", 0),
          ("kbps", 1))
    )


_IfStormControlMode_Type.__name__ = "Integer32"
_IfStormControlMode_Object = MibTableColumn
ifStormControlMode = _IfStormControlMode_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 2, 1, 9),
    _IfStormControlMode_Type()
)
ifStormControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifStormControlMode.setStatus("mandatory")


class _IfStormControlEnable_Type(Bits):
    """Custom type ifStormControlEnable based on Bits"""
    namedValues = NamedValues(
        *(("log", 0),
          ("trap", 1))
    )

_IfStormControlEnable_Type.__name__ = "Bits"
_IfStormControlEnable_Object = MibTableColumn
ifStormControlEnable = _IfStormControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 2, 1, 10),
    _IfStormControlEnable_Type()
)
ifStormControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifStormControlEnable.setStatus("mandatory")
_IfSfpParameterTable_Object = MibTable
ifSfpParameterTable = _IfSfpParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7)
)
if mibBuilder.loadTexts:
    ifSfpParameterTable.setStatus("mandatory")
_IfSfpParameterEntry_Object = MibTableRow
ifSfpParameterEntry = _IfSfpParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1)
)
ifSfpParameterEntry.setIndexNames(
    (0, "NMS-IF-MIB", "ifSfpIndex"),
)
if mibBuilder.loadTexts:
    ifSfpParameterEntry.setStatus("mandatory")
_IfSfpIndex_Type = Integer32
_IfSfpIndex_Object = MibTableColumn
ifSfpIndex = _IfSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 1),
    _IfSfpIndex_Type()
)
ifSfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSfpIndex.setStatus("mandatory")
_TxPower1_Type = Integer32
_TxPower1_Object = MibTableColumn
txPower1 = _TxPower1_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 2),
    _TxPower1_Type()
)
txPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txPower1.setStatus("mandatory")
_RxPower1_Type = Integer32
_RxPower1_Object = MibTableColumn
rxPower1 = _RxPower1_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 3),
    _RxPower1_Type()
)
rxPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPower1.setStatus("mandatory")
_Temperature_Type = Integer32
_Temperature_Object = MibTableColumn
temperature = _Temperature_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 4),
    _Temperature_Type()
)
temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature.setStatus("mandatory")
_Vlotage_Type = Integer32
_Vlotage_Object = MibTableColumn
vlotage = _Vlotage_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 5),
    _Vlotage_Type()
)
vlotage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlotage.setStatus("mandatory")
_Curr1_Type = Integer32
_Curr1_Object = MibTableColumn
curr1 = _Curr1_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 6),
    _Curr1_Type()
)
curr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curr1.setStatus("mandatory")
_Vendname_Type = OctetString
_Vendname_Object = MibTableColumn
vendname = _Vendname_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 7),
    _Vendname_Type()
)
vendname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vendname.setStatus("mandatory")
_TxPower2_Type = Integer32
_TxPower2_Object = MibTableColumn
txPower2 = _TxPower2_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 8),
    _TxPower2_Type()
)
txPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txPower2.setStatus("mandatory")
_RxPower2_Type = Integer32
_RxPower2_Object = MibTableColumn
rxPower2 = _RxPower2_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 9),
    _RxPower2_Type()
)
rxPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPower2.setStatus("mandatory")
_Curr2_Type = Integer32
_Curr2_Object = MibTableColumn
curr2 = _Curr2_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 10),
    _Curr2_Type()
)
curr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curr2.setStatus("mandatory")
_TxPower3_Type = Integer32
_TxPower3_Object = MibTableColumn
txPower3 = _TxPower3_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 11),
    _TxPower3_Type()
)
txPower3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txPower3.setStatus("mandatory")
_RxPower3_Type = Integer32
_RxPower3_Object = MibTableColumn
rxPower3 = _RxPower3_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 12),
    _RxPower3_Type()
)
rxPower3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPower3.setStatus("mandatory")
_Curr3_Type = Integer32
_Curr3_Object = MibTableColumn
curr3 = _Curr3_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 13),
    _Curr3_Type()
)
curr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curr3.setStatus("mandatory")
_TxPower4_Type = Integer32
_TxPower4_Object = MibTableColumn
txPower4 = _TxPower4_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 14),
    _TxPower4_Type()
)
txPower4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txPower4.setStatus("mandatory")
_RxPower4_Type = Integer32
_RxPower4_Object = MibTableColumn
rxPower4 = _RxPower4_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 15),
    _RxPower4_Type()
)
rxPower4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPower4.setStatus("mandatory")
_Curr4_Type = Integer32
_Curr4_Object = MibTableColumn
curr4 = _Curr4_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 16),
    _Curr4_Type()
)
curr4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curr4.setStatus("mandatory")


class _Type_Type(Integer32):
    """Custom type type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sfp", 1),
          ("copper-sfp", 2),
          ("other", 3))
    )


_Type_Type.__name__ = "Integer32"
_Type_Object = MibTableColumn
type = _Type_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 17),
    _Type_Type()
)
type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    type.setStatus("mandatory")
_TransDist_Type = Integer32
_TransDist_Object = MibTableColumn
transDist = _TransDist_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 18),
    _TransDist_Type()
)
transDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transDist.setStatus("mandatory")
_WaveLen_Type = Integer32
_WaveLen_Object = MibTableColumn
waveLen = _WaveLen_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 19),
    _WaveLen_Type()
)
waveLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waveLen.setStatus("mandatory")


class _SfpPresentStatus_Type(Integer32):
    """Custom type sfpPresentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("online", 1),
          ("offline", 2))
    )


_SfpPresentStatus_Type.__name__ = "Integer32"
_SfpPresentStatus_Object = MibTableColumn
sfpPresentStatus = _SfpPresentStatus_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 20),
    _SfpPresentStatus_Type()
)
sfpPresentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpPresentStatus.setStatus("mandatory")


class _SfpLostStatus_Type(Integer32):
    """Custom type sfpLostStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("lost", 2))
    )


_SfpLostStatus_Type.__name__ = "Integer32"
_SfpLostStatus_Object = MibTableColumn
sfpLostStatus = _SfpLostStatus_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 21),
    _SfpLostStatus_Type()
)
sfpLostStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpLostStatus.setStatus("mandatory")


class _SfpMismatchStatus_Type(Integer32):
    """Custom type sfpMismatchStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("match", 1),
          ("mismatch", 2))
    )


_SfpMismatchStatus_Type.__name__ = "Integer32"
_SfpMismatchStatus_Object = MibTableColumn
sfpMismatchStatus = _SfpMismatchStatus_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 22),
    _SfpMismatchStatus_Type()
)
sfpMismatchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpMismatchStatus.setStatus("mandatory")
_SfpSeqNum_Type = OctetString
_SfpSeqNum_Object = MibTableColumn
sfpSeqNum = _SfpSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 23),
    _SfpSeqNum_Type()
)
sfpSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpSeqNum.setStatus("mandatory")
_VoltageHighAlarm_Type = Integer32
_VoltageHighAlarm_Object = MibTableColumn
voltageHighAlarm = _VoltageHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 24),
    _VoltageHighAlarm_Type()
)
voltageHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageHighAlarm.setStatus("mandatory")
_VoltageHighWarning_Type = Integer32
_VoltageHighWarning_Object = MibTableColumn
voltageHighWarning = _VoltageHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 25),
    _VoltageHighWarning_Type()
)
voltageHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageHighWarning.setStatus("mandatory")
_VoltageLowWarning_Type = Integer32
_VoltageLowWarning_Object = MibTableColumn
voltageLowWarning = _VoltageLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 26),
    _VoltageLowWarning_Type()
)
voltageLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageLowWarning.setStatus("mandatory")
_VoltageLowAlarm_Type = Integer32
_VoltageLowAlarm_Object = MibTableColumn
voltageLowAlarm = _VoltageLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 27),
    _VoltageLowAlarm_Type()
)
voltageLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageLowAlarm.setStatus("mandatory")
_TemperatureHighAlarm_Type = Integer32
_TemperatureHighAlarm_Object = MibTableColumn
temperatureHighAlarm = _TemperatureHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 28),
    _TemperatureHighAlarm_Type()
)
temperatureHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureHighAlarm.setStatus("mandatory")
_TemperatureHighWarning_Type = Integer32
_TemperatureHighWarning_Object = MibTableColumn
temperatureHighWarning = _TemperatureHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 29),
    _TemperatureHighWarning_Type()
)
temperatureHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureHighWarning.setStatus("mandatory")
_TemperatureLowWarning_Type = Integer32
_TemperatureLowWarning_Object = MibTableColumn
temperatureLowWarning = _TemperatureLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 30),
    _TemperatureLowWarning_Type()
)
temperatureLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureLowWarning.setStatus("mandatory")
_TemperatureLowAlarm_Type = Integer32
_TemperatureLowAlarm_Object = MibTableColumn
temperatureLowAlarm = _TemperatureLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 31),
    _TemperatureLowAlarm_Type()
)
temperatureLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureLowAlarm.setStatus("mandatory")
_BiasHighAlarm_Type = Integer32
_BiasHighAlarm_Object = MibTableColumn
biasHighAlarm = _BiasHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 32),
    _BiasHighAlarm_Type()
)
biasHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biasHighAlarm.setStatus("mandatory")
_BiasHighWarning_Type = Integer32
_BiasHighWarning_Object = MibTableColumn
biasHighWarning = _BiasHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 33),
    _BiasHighWarning_Type()
)
biasHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biasHighWarning.setStatus("mandatory")
_BiasLowWarning_Type = Integer32
_BiasLowWarning_Object = MibTableColumn
biasLowWarning = _BiasLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 34),
    _BiasLowWarning_Type()
)
biasLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biasLowWarning.setStatus("mandatory")
_BiasLowAlarm_Type = Integer32
_BiasLowAlarm_Object = MibTableColumn
biasLowAlarm = _BiasLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 35),
    _BiasLowAlarm_Type()
)
biasLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biasLowAlarm.setStatus("mandatory")
_TxPowerHighAlarm_Type = Integer32
_TxPowerHighAlarm_Object = MibTableColumn
txPowerHighAlarm = _TxPowerHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 36),
    _TxPowerHighAlarm_Type()
)
txPowerHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txPowerHighAlarm.setStatus("mandatory")
_TxPowerHighWarning_Type = Integer32
_TxPowerHighWarning_Object = MibTableColumn
txPowerHighWarning = _TxPowerHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 37),
    _TxPowerHighWarning_Type()
)
txPowerHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txPowerHighWarning.setStatus("mandatory")
_TxPowerLowWarning_Type = Integer32
_TxPowerLowWarning_Object = MibTableColumn
txPowerLowWarning = _TxPowerLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 38),
    _TxPowerLowWarning_Type()
)
txPowerLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txPowerLowWarning.setStatus("mandatory")
_TxPowerLowAlarm_Type = Integer32
_TxPowerLowAlarm_Object = MibTableColumn
txPowerLowAlarm = _TxPowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 39),
    _TxPowerLowAlarm_Type()
)
txPowerLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txPowerLowAlarm.setStatus("mandatory")
_RxPowerHighAlarm_Type = Integer32
_RxPowerHighAlarm_Object = MibTableColumn
rxPowerHighAlarm = _RxPowerHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 40),
    _RxPowerHighAlarm_Type()
)
rxPowerHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPowerHighAlarm.setStatus("mandatory")
_RxPowerHighWarning_Type = Integer32
_RxPowerHighWarning_Object = MibTableColumn
rxPowerHighWarning = _RxPowerHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 41),
    _RxPowerHighWarning_Type()
)
rxPowerHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPowerHighWarning.setStatus("mandatory")
_RxPowerLowWarning_Type = Integer32
_RxPowerLowWarning_Object = MibTableColumn
rxPowerLowWarning = _RxPowerLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 42),
    _RxPowerLowWarning_Type()
)
rxPowerLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPowerLowWarning.setStatus("mandatory")
_RxPowerLowAlarm_Type = Integer32
_RxPowerLowAlarm_Object = MibTableColumn
rxPowerLowAlarm = _RxPowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 43),
    _RxPowerLowAlarm_Type()
)
rxPowerLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPowerLowAlarm.setStatus("mandatory")
_VendorPN_Type = OctetString
_VendorPN_Object = MibTableColumn
vendorPN = _VendorPN_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 7, 1, 44),
    _VendorPN_Type()
)
vendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vendorPN.setStatus("mandatory")
_CableDiagnoseTable_Object = MibTable
cableDiagnoseTable = _CableDiagnoseTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 8)
)
if mibBuilder.loadTexts:
    cableDiagnoseTable.setStatus("mandatory")
_CableDiagnoseEntry_Object = MibTableRow
cableDiagnoseEntry = _CableDiagnoseEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 8, 1)
)
cableDiagnoseEntry.setIndexNames(
    (0, "NMS-IF-MIB", "cableDiagIfIndex"),
)
if mibBuilder.loadTexts:
    cableDiagnoseEntry.setStatus("mandatory")
_CableDiagIfIndex_Type = Integer32
_CableDiagIfIndex_Object = MibTableColumn
cableDiagIfIndex = _CableDiagIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 8, 1, 1),
    _CableDiagIfIndex_Type()
)
cableDiagIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagIfIndex.setStatus("mandatory")
_CableDiagnoseResult_Type = OctetString
_CableDiagnoseResult_Object = MibTableColumn
cableDiagnoseResult = _CableDiagnoseResult_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 8, 1, 2),
    _CableDiagnoseResult_Type()
)
cableDiagnoseResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagnoseResult.setStatus("mandatory")
_IfportMtuTable_Object = MibTable
ifportMtuTable = _IfportMtuTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 9)
)
if mibBuilder.loadTexts:
    ifportMtuTable.setStatus("mandatory")
_IfportMtuEntry_Object = MibTableRow
ifportMtuEntry = _IfportMtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 9, 1)
)
ifportMtuEntry.setIndexNames(
    (0, "NMS-IF-MIB", "ifportMtuIndex"),
)
if mibBuilder.loadTexts:
    ifportMtuEntry.setStatus("mandatory")
_IfportMtuIndex_Type = Integer32
_IfportMtuIndex_Object = MibTableColumn
ifportMtuIndex = _IfportMtuIndex_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 9, 1, 1),
    _IfportMtuIndex_Type()
)
ifportMtuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifportMtuIndex.setStatus("mandatory")
_IfportMtuJumbo_Type = Integer32
_IfportMtuJumbo_Object = MibTableColumn
ifportMtuJumbo = _IfportMtuJumbo_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 9, 1, 2),
    _IfportMtuJumbo_Type()
)
ifportMtuJumbo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifportMtuJumbo.setStatus("mandatory")
_StormctlWarning_ObjectIdentity = ObjectIdentity
stormctlWarning = _StormctlWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 10)
)
_StormctlWarningGroup_ObjectIdentity = ObjectIdentity
stormctlWarningGroup = _StormctlWarningGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 10, 1)
)
_StormctlWarningIfindex_Type = Integer32
_StormctlWarningIfindex_Object = MibScalar
stormctlWarningIfindex = _StormctlWarningIfindex_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 10, 1, 1),
    _StormctlWarningIfindex_Type()
)
stormctlWarningIfindex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    stormctlWarningIfindex.setStatus("mandatory")
_StormctlWarningIfDescr_Type = DisplayString
_StormctlWarningIfDescr_Object = MibScalar
stormctlWarningIfDescr = _StormctlWarningIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 10, 1, 2),
    _StormctlWarningIfDescr_Type()
)
stormctlWarningIfDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    stormctlWarningIfDescr.setStatus("mandatory")


class _StormctlWarningType_Type(Integer32):
    """Custom type stormctlWarningType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("multicast", 2))
    )


_StormctlWarningType_Type.__name__ = "Integer32"
_StormctlWarningType_Object = MibScalar
stormctlWarningType = _StormctlWarningType_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 10, 1, 3),
    _StormctlWarningType_Type()
)
stormctlWarningType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    stormctlWarningType.setStatus("mandatory")
_StormctlWarningInfo_Type = DisplayString
_StormctlWarningInfo_Object = MibScalar
stormctlWarningInfo = _StormctlWarningInfo_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 10, 1, 4),
    _StormctlWarningInfo_Type()
)
stormctlWarningInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    stormctlWarningInfo.setStatus("mandatory")
_StormctlWarningNotifications_ObjectIdentity = ObjectIdentity
stormctlWarningNotifications = _StormctlWarningNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 10, 2)
)
_TrafficNotify_ObjectIdentity = ObjectIdentity
trafficNotify = _TrafficNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 11)
)
_TrafficNotifyGroup_ObjectIdentity = ObjectIdentity
trafficNotifyGroup = _TrafficNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 11, 1)
)
_TrafficNotifyIfIndex_Type = Integer32
_TrafficNotifyIfIndex_Object = MibScalar
trafficNotifyIfIndex = _TrafficNotifyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 11, 1, 1),
    _TrafficNotifyIfIndex_Type()
)
trafficNotifyIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trafficNotifyIfIndex.setStatus("mandatory")
_TrafficNotifyIfDescr_Type = DisplayString
_TrafficNotifyIfDescr_Object = MibScalar
trafficNotifyIfDescr = _TrafficNotifyIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 11, 1, 2),
    _TrafficNotifyIfDescr_Type()
)
trafficNotifyIfDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trafficNotifyIfDescr.setStatus("mandatory")


class _TrafficNotifyType_Type(Integer32):
    """Custom type trafficNotifyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exceed", 1),
          ("resume", 2))
    )


_TrafficNotifyType_Type.__name__ = "Integer32"
_TrafficNotifyType_Object = MibScalar
trafficNotifyType = _TrafficNotifyType_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 11, 1, 3),
    _TrafficNotifyType_Type()
)
trafficNotifyType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trafficNotifyType.setStatus("mandatory")
_TrafficNotifyInfo_Type = DisplayString
_TrafficNotifyInfo_Object = MibScalar
trafficNotifyInfo = _TrafficNotifyInfo_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 11, 1, 4),
    _TrafficNotifyInfo_Type()
)
trafficNotifyInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trafficNotifyInfo.setStatus("mandatory")
_TrafficNotifyNotifications_ObjectIdentity = ObjectIdentity
trafficNotifyNotifications = _TrafficNotifyNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 11, 2)
)
_TrafficNotifyConfig_ObjectIdentity = ObjectIdentity
trafficNotifyConfig = _TrafficNotifyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 11, 3)
)


class _TrafficNotifyAction_Type(Bits):
    """Custom type trafficNotifyAction based on Bits"""
    namedValues = NamedValues(
        *(("syslog", 0),
          ("snmp-trap", 1))
    )

_TrafficNotifyAction_Type.__name__ = "Bits"
_TrafficNotifyAction_Object = MibScalar
trafficNotifyAction = _TrafficNotifyAction_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 11, 3, 1),
    _TrafficNotifyAction_Type()
)
trafficNotifyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficNotifyAction.setStatus("mandatory")


class _TrafficNotifyInterval_Type(Integer32):
    """Custom type trafficNotifyInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_TrafficNotifyInterval_Type.__name__ = "Integer32"
_TrafficNotifyInterval_Object = MibScalar
trafficNotifyInterval = _TrafficNotifyInterval_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 11, 3, 2),
    _TrafficNotifyInterval_Type()
)
trafficNotifyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficNotifyInterval.setStatus("mandatory")
_IfTrafficNotifyTable_Object = MibTable
ifTrafficNotifyTable = _IfTrafficNotifyTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 12)
)
if mibBuilder.loadTexts:
    ifTrafficNotifyTable.setStatus("mandatory")
_IfTrafficNotifyEntry_Object = MibTableRow
ifTrafficNotifyEntry = _IfTrafficNotifyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 12, 1)
)
ifTrafficNotifyEntry.setIndexNames(
    (0, "NMS-IF-MIB", "ifTrafficNotifyIndex"),
)
if mibBuilder.loadTexts:
    ifTrafficNotifyEntry.setStatus("mandatory")
_IfTrafficNotifyIndex_Type = Integer32
_IfTrafficNotifyIndex_Object = MibTableColumn
ifTrafficNotifyIndex = _IfTrafficNotifyIndex_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 12, 1, 1),
    _IfTrafficNotifyIndex_Type()
)
ifTrafficNotifyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTrafficNotifyIndex.setStatus("mandatory")


class _IfTrafficNotifyInHighRate_Type(Integer32):
    """Custom type ifTrafficNotifyInHighRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IfTrafficNotifyInHighRate_Type.__name__ = "Integer32"
_IfTrafficNotifyInHighRate_Object = MibTableColumn
ifTrafficNotifyInHighRate = _IfTrafficNotifyInHighRate_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 12, 1, 2),
    _IfTrafficNotifyInHighRate_Type()
)
ifTrafficNotifyInHighRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTrafficNotifyInHighRate.setStatus("mandatory")


class _IfTrafficNotifyInResumeRate_Type(Integer32):
    """Custom type ifTrafficNotifyInResumeRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IfTrafficNotifyInResumeRate_Type.__name__ = "Integer32"
_IfTrafficNotifyInResumeRate_Object = MibTableColumn
ifTrafficNotifyInResumeRate = _IfTrafficNotifyInResumeRate_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 12, 1, 3),
    _IfTrafficNotifyInResumeRate_Type()
)
ifTrafficNotifyInResumeRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTrafficNotifyInResumeRate.setStatus("mandatory")


class _IfTrafficNotifyOutHighRate_Type(Integer32):
    """Custom type ifTrafficNotifyOutHighRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IfTrafficNotifyOutHighRate_Type.__name__ = "Integer32"
_IfTrafficNotifyOutHighRate_Object = MibTableColumn
ifTrafficNotifyOutHighRate = _IfTrafficNotifyOutHighRate_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 12, 1, 4),
    _IfTrafficNotifyOutHighRate_Type()
)
ifTrafficNotifyOutHighRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTrafficNotifyOutHighRate.setStatus("mandatory")


class _IfTrafficNotifyOutResumeRate_Type(Integer32):
    """Custom type ifTrafficNotifyOutResumeRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IfTrafficNotifyOutResumeRate_Type.__name__ = "Integer32"
_IfTrafficNotifyOutResumeRate_Object = MibTableColumn
ifTrafficNotifyOutResumeRate = _IfTrafficNotifyOutResumeRate_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 12, 1, 5),
    _IfTrafficNotifyOutResumeRate_Type()
)
ifTrafficNotifyOutResumeRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTrafficNotifyOutResumeRate.setStatus("mandatory")
_PortSecurityViolationNotify_ObjectIdentity = ObjectIdentity
portSecurityViolationNotify = _PortSecurityViolationNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 13)
)
_PortSecurityViolationNotifyGroup_ObjectIdentity = ObjectIdentity
portSecurityViolationNotifyGroup = _PortSecurityViolationNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 13, 1)
)
_PortSecurityViolationNotifyIfindex_Type = Integer32
_PortSecurityViolationNotifyIfindex_Object = MibScalar
portSecurityViolationNotifyIfindex = _PortSecurityViolationNotifyIfindex_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 13, 1, 1),
    _PortSecurityViolationNotifyIfindex_Type()
)
portSecurityViolationNotifyIfindex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    portSecurityViolationNotifyIfindex.setStatus("mandatory")
_PortSecurityViolationNotifyIfDescr_Type = DisplayString
_PortSecurityViolationNotifyIfDescr_Object = MibScalar
portSecurityViolationNotifyIfDescr = _PortSecurityViolationNotifyIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 13, 1, 2),
    _PortSecurityViolationNotifyIfDescr_Type()
)
portSecurityViolationNotifyIfDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    portSecurityViolationNotifyIfDescr.setStatus("mandatory")
_PortSecurityViolationNotifyInfo_Type = DisplayString
_PortSecurityViolationNotifyInfo_Object = MibScalar
portSecurityViolationNotifyInfo = _PortSecurityViolationNotifyInfo_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 13, 1, 3),
    _PortSecurityViolationNotifyInfo_Type()
)
portSecurityViolationNotifyInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    portSecurityViolationNotifyInfo.setStatus("mandatory")
_PortSecurityViolationNotifyNotifications_ObjectIdentity = ObjectIdentity
portSecurityViolationNotifyNotifications = _PortSecurityViolationNotifyNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 13, 2)
)
_PhysicalIfConfig2Table_Object = MibTable
physicalIfConfig2Table = _PhysicalIfConfig2Table_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 14)
)
if mibBuilder.loadTexts:
    physicalIfConfig2Table.setStatus("mandatory")
_PhysicalIfConfig2Entry_Object = MibTableRow
physicalIfConfig2Entry = _PhysicalIfConfig2Entry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 14, 1)
)
physicalIfConfig2Entry.setIndexNames(
    (0, "NMS-IF-MIB", "ifConfigIndex"),
)
if mibBuilder.loadTexts:
    physicalIfConfig2Entry.setStatus("mandatory")
_IfConfigIndex_Type = Integer32
_IfConfigIndex_Object = MibTableColumn
ifConfigIndex = _IfConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 14, 1, 1),
    _IfConfigIndex_Type()
)
ifConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifConfigIndex.setStatus("mandatory")


class _FiberAutoConfig_Type(Integer32):
    """Custom type fiberAutoConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FiberAutoConfig_Type.__name__ = "Integer32"
_FiberAutoConfig_Object = MibTableColumn
fiberAutoConfig = _FiberAutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 14, 1, 2),
    _FiberAutoConfig_Type()
)
fiberAutoConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fiberAutoConfig.setStatus("mandatory")


class _AutoNegoConfig_Type(Integer32):
    """Custom type autoNegoConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AutoNegoConfig_Type.__name__ = "Integer32"
_AutoNegoConfig_Object = MibTableColumn
autoNegoConfig = _AutoNegoConfig_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 14, 1, 3),
    _AutoNegoConfig_Type()
)
autoNegoConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoNegoConfig.setStatus("mandatory")


class _SpeedConfig_Type(Integer32):
    """Custom type speedConfig based on Integer32"""
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
        *(("speed-10M", 1),
          ("speed-100M", 2),
          ("speed-1000M", 3),
          ("speed-10000M", 4),
          ("speed-40000M", 5),
          ("speed-100000M", 6))
    )


_SpeedConfig_Type.__name__ = "Integer32"
_SpeedConfig_Object = MibTableColumn
speedConfig = _SpeedConfig_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 14, 1, 4),
    _SpeedConfig_Type()
)
speedConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedConfig.setStatus("mandatory")


class _DuplexConfig_Type(Integer32):
    """Custom type duplexConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2))
    )


_DuplexConfig_Type.__name__ = "Integer32"
_DuplexConfig_Object = MibTableColumn
duplexConfig = _DuplexConfig_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 14, 1, 5),
    _DuplexConfig_Type()
)
duplexConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    duplexConfig.setStatus("mandatory")

# Managed Objects groups


# Notification objects

stormctlWarningNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 10, 2, 1)
)
stormctlWarningNotification.setObjects(
      *(("NMS-IF-MIB", "stormctlWarningIfindex"),
        ("NMS-IF-MIB", "stormctlWarningIfDescr"),
        ("NMS-IF-MIB", "stormctlWarningType"),
        ("NMS-IF-MIB", "stormctlWarningInfo"))
)
if mibBuilder.loadTexts:
    stormctlWarningNotification.setStatus(
        "mandatory"
    )

trafficNotifyNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 11, 2, 1)
)
trafficNotifyNotification.setObjects(
      *(("NMS-IF-MIB", "trafficNotifyIfindex"),
        ("NMS-IF-MIB", "trafficNotifyIfDescr"),
        ("NMS-IF-MIB", "trafficNotifyType"),
        ("NMS-IF-MIB", "trafficNotifyInfo"))
)
if mibBuilder.loadTexts:
    trafficNotifyNotification.setStatus(
        "mandatory"
    )

portSecurityViolationNotifyNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3320, 9, 63, 1, 13, 2, 1)
)
portSecurityViolationNotifyNotification.setObjects(
      *(("NMS-IF-MIB", "portSecurityViolationNotifyIfindex"),
        ("NMS-IF-MIB", "portSecurityViolationNotifyIfDescr"),
        ("NMS-IF-MIB", "portSecurityViolationNotifyInfo"))
)
if mibBuilder.loadTexts:
    portSecurityViolationNotifyNotification.setStatus(
        "mandatory"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-IF-MIB",
    **{"nmsIfMIB": nmsIfMIB,
       "nmsIfObjects": nmsIfObjects,
       "vifTable": vifTable,
       "vifEntry": vifEntry,
       "vifIndex": vifIndex,
       "vifDescr": vifDescr,
       "vifType": vifType,
       "vifMtu": vifMtu,
       "vifSpeed": vifSpeed,
       "vifPhysAddress": vifPhysAddress,
       "vifAdminStatus": vifAdminStatus,
       "vifOperStatus": vifOperStatus,
       "vifLastChange": vifLastChange,
       "ifStormControlTable": ifStormControlTable,
       "ifStormControlEntry": ifStormControlEntry,
       "ifIndex": ifIndex,
       "ifStormControlBroadcast": ifStormControlBroadcast,
       "ifStormControlMulticast": ifStormControlMulticast,
       "ifStormControlUnicast": ifStormControlUnicast,
       "ifStormControlBroadcastAction": ifStormControlBroadcastAction,
       "ifStormControlBroadcastAutoResume": ifStormControlBroadcastAutoResume,
       "ifStormControlMulticastAction": ifStormControlMulticastAction,
       "ifStormControlMulticastAutoResume": ifStormControlMulticastAutoResume,
       "ifStormControlMode": ifStormControlMode,
       "ifStormControlEnable": ifStormControlEnable,
       "ifSfpParameterTable": ifSfpParameterTable,
       "ifSfpParameterEntry": ifSfpParameterEntry,
       "ifSfpIndex": ifSfpIndex,
       "txPower1": txPower1,
       "rxPower1": rxPower1,
       "temperature": temperature,
       "vlotage": vlotage,
       "curr1": curr1,
       "vendname": vendname,
       "txPower2": txPower2,
       "rxPower2": rxPower2,
       "curr2": curr2,
       "txPower3": txPower3,
       "rxPower3": rxPower3,
       "curr3": curr3,
       "txPower4": txPower4,
       "rxPower4": rxPower4,
       "curr4": curr4,
       "type": type,
       "transDist": transDist,
       "waveLen": waveLen,
       "sfpPresentStatus": sfpPresentStatus,
       "sfpLostStatus": sfpLostStatus,
       "sfpMismatchStatus": sfpMismatchStatus,
       "sfpSeqNum": sfpSeqNum,
       "voltageHighAlarm": voltageHighAlarm,
       "voltageHighWarning": voltageHighWarning,
       "voltageLowWarning": voltageLowWarning,
       "voltageLowAlarm": voltageLowAlarm,
       "temperatureHighAlarm": temperatureHighAlarm,
       "temperatureHighWarning": temperatureHighWarning,
       "temperatureLowWarning": temperatureLowWarning,
       "temperatureLowAlarm": temperatureLowAlarm,
       "biasHighAlarm": biasHighAlarm,
       "biasHighWarning": biasHighWarning,
       "biasLowWarning": biasLowWarning,
       "biasLowAlarm": biasLowAlarm,
       "txPowerHighAlarm": txPowerHighAlarm,
       "txPowerHighWarning": txPowerHighWarning,
       "txPowerLowWarning": txPowerLowWarning,
       "txPowerLowAlarm": txPowerLowAlarm,
       "rxPowerHighAlarm": rxPowerHighAlarm,
       "rxPowerHighWarning": rxPowerHighWarning,
       "rxPowerLowWarning": rxPowerLowWarning,
       "rxPowerLowAlarm": rxPowerLowAlarm,
       "vendorPN": vendorPN,
       "cableDiagnoseTable": cableDiagnoseTable,
       "cableDiagnoseEntry": cableDiagnoseEntry,
       "cableDiagIfIndex": cableDiagIfIndex,
       "cableDiagnoseResult": cableDiagnoseResult,
       "ifportMtuTable": ifportMtuTable,
       "ifportMtuEntry": ifportMtuEntry,
       "ifportMtuIndex": ifportMtuIndex,
       "ifportMtuJumbo": ifportMtuJumbo,
       "stormctlWarning": stormctlWarning,
       "stormctlWarningGroup": stormctlWarningGroup,
       "stormctlWarningIfindex": stormctlWarningIfindex,
       "stormctlWarningIfDescr": stormctlWarningIfDescr,
       "stormctlWarningType": stormctlWarningType,
       "stormctlWarningInfo": stormctlWarningInfo,
       "stormctlWarningNotifications": stormctlWarningNotifications,
       "stormctlWarningNotification": stormctlWarningNotification,
       "trafficNotify": trafficNotify,
       "trafficNotifyGroup": trafficNotifyGroup,
       "trafficNotifyIfIndex": trafficNotifyIfIndex,
       "trafficNotifyIfDescr": trafficNotifyIfDescr,
       "trafficNotifyType": trafficNotifyType,
       "trafficNotifyInfo": trafficNotifyInfo,
       "trafficNotifyNotifications": trafficNotifyNotifications,
       "trafficNotifyNotification": trafficNotifyNotification,
       "trafficNotifyConfig": trafficNotifyConfig,
       "trafficNotifyAction": trafficNotifyAction,
       "trafficNotifyInterval": trafficNotifyInterval,
       "ifTrafficNotifyTable": ifTrafficNotifyTable,
       "ifTrafficNotifyEntry": ifTrafficNotifyEntry,
       "ifTrafficNotifyIndex": ifTrafficNotifyIndex,
       "ifTrafficNotifyInHighRate": ifTrafficNotifyInHighRate,
       "ifTrafficNotifyInResumeRate": ifTrafficNotifyInResumeRate,
       "ifTrafficNotifyOutHighRate": ifTrafficNotifyOutHighRate,
       "ifTrafficNotifyOutResumeRate": ifTrafficNotifyOutResumeRate,
       "portSecurityViolationNotify": portSecurityViolationNotify,
       "portSecurityViolationNotifyGroup": portSecurityViolationNotifyGroup,
       "portSecurityViolationNotifyIfindex": portSecurityViolationNotifyIfindex,
       "portSecurityViolationNotifyIfDescr": portSecurityViolationNotifyIfDescr,
       "portSecurityViolationNotifyInfo": portSecurityViolationNotifyInfo,
       "portSecurityViolationNotifyNotifications": portSecurityViolationNotifyNotifications,
       "portSecurityViolationNotifyNotification": portSecurityViolationNotifyNotification,
       "physicalIfConfig2Table": physicalIfConfig2Table,
       "physicalIfConfig2Entry": physicalIfConfig2Entry,
       "ifConfigIndex": ifConfigIndex,
       "fiberAutoConfig": fiberAutoConfig,
       "autoNegoConfig": autoNegoConfig,
       "speedConfig": speedConfig,
       "duplexConfig": duplexConfig}
)
