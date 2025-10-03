# SNMP MIB module (XAVI-XG6846-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\inteno\XAVI-XG6846-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:01:52 2025
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

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 enterprises,
 iso,
 mib_2,
 snmpModules) = mibBuilder.importSymbols(
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
    "enterprises",
    "iso",
    "mib-2",
    "snmpModules")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TestAndIncr,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Xg6846_ObjectIdentity = ObjectIdentity
xg6846 = _Xg6846_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12919)
)
_Catv_ObjectIdentity = ObjectIdentity
catv = _Catv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12919, 1)
)


class _CatvEnable_Type(Integer32):
    """Custom type catvEnable based on Integer32"""
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


_CatvEnable_Type.__name__ = "Integer32"
_CatvEnable_Object = MibScalar
catvEnable = _CatvEnable_Object(
    (1, 3, 6, 1, 4, 1, 12919, 1, 1),
    _CatvEnable_Type()
)
catvEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    catvEnable.setStatus("current")
_Portmode_ObjectIdentity = ObjectIdentity
portmode = _Portmode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12919, 2)
)
_LanportTable_Object = MibTable
lanportTable = _LanportTable_Object(
    (1, 3, 6, 1, 4, 1, 12919, 2, 1)
)
if mibBuilder.loadTexts:
    lanportTable.setStatus("current")
_ModeEntry_Object = MibTableRow
modeEntry = _ModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 12919, 2, 1, 1)
)
modeEntry.setIndexNames(
    (0, "XAVI-XG6846-MIB", "lanportIndex"),
)
if mibBuilder.loadTexts:
    modeEntry.setStatus("current")
_LanportIndex_Type = Unsigned32
_LanportIndex_Object = MibTableColumn
lanportIndex = _LanportIndex_Object(
    (1, 3, 6, 1, 4, 1, 12919, 2, 1, 1, 1),
    _LanportIndex_Type()
)
lanportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanportIndex.setStatus("current")
_LanportName_Type = DisplayString
_LanportName_Object = MibTableColumn
lanportName = _LanportName_Object(
    (1, 3, 6, 1, 4, 1, 12919, 2, 1, 1, 2),
    _LanportName_Type()
)
lanportName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanportName.setStatus("current")


class _Lanportspeed_Type(Integer32):
    """Custom type lanportspeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("speed10mFD", 1),
          ("speed10mHD", 2),
          ("speed100mFD", 3),
          ("speed100mHD", 4))
    )


_Lanportspeed_Type.__name__ = "Integer32"
_Lanportspeed_Object = MibTableColumn
lanportspeed = _Lanportspeed_Object(
    (1, 3, 6, 1, 4, 1, 12919, 2, 1, 1, 3),
    _Lanportspeed_Type()
)
lanportspeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanportspeed.setStatus("current")


class _Lanportpause_Type(Integer32):
    """Custom type lanportpause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Lanportpause_Type.__name__ = "Integer32"
_Lanportpause_Object = MibTableColumn
lanportpause = _Lanportpause_Object(
    (1, 3, 6, 1, 4, 1, 12919, 2, 1, 1, 4),
    _Lanportpause_Type()
)
lanportpause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanportpause.setStatus("current")
_Qos_ObjectIdentity = ObjectIdentity
qos = _Qos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12919, 3)
)
_QosTable_Object = MibTable
qosTable = _QosTable_Object(
    (1, 3, 6, 1, 4, 1, 12919, 3, 1)
)
if mibBuilder.loadTexts:
    qosTable.setStatus("current")
_QosEntry_Object = MibTableRow
qosEntry = _QosEntry_Object(
    (1, 3, 6, 1, 4, 1, 12919, 3, 1, 1)
)
qosEntry.setIndexNames(
    (0, "XAVI-XG6846-MIB", "qosIndex"),
)
if mibBuilder.loadTexts:
    qosEntry.setStatus("current")
_QosIndex_Type = Unsigned32
_QosIndex_Object = MibTableColumn
qosIndex = _QosIndex_Object(
    (1, 3, 6, 1, 4, 1, 12919, 3, 1, 1, 1),
    _QosIndex_Type()
)
qosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIndex.setStatus("current")
_Qmapping_Type = Unsigned32
_Qmapping_Object = MibTableColumn
qmapping = _Qmapping_Object(
    (1, 3, 6, 1, 4, 1, 12919, 3, 1, 1, 2),
    _Qmapping_Type()
)
qmapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmapping.setStatus("current")
_Vlan_ObjectIdentity = ObjectIdentity
vlan = _Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12919, 4)
)
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 12919, 4, 1)
)
if mibBuilder.loadTexts:
    portTable.setStatus("current")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 12919, 4, 1, 1)
)
portEntry.setIndexNames(
    (0, "XAVI-XG6846-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("current")
_PortIndex_Type = Unsigned32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 12919, 4, 1, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("current")
_Vlanid_Type = Unsigned32
_Vlanid_Object = MibTableColumn
vlanid = _Vlanid_Object(
    (1, 3, 6, 1, 4, 1, 12919, 4, 1, 1, 2),
    _Vlanid_Type()
)
vlanid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanid.setStatus("current")
_Priority_Type = Unsigned32
_Priority_Object = MibTableColumn
priority = _Priority_Object(
    (1, 3, 6, 1, 4, 1, 12919, 4, 1, 1, 3),
    _Priority_Type()
)
priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priority.setStatus("current")


class _Qmode_Type(Integer32):
    """Custom type qmode based on Integer32"""
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
        *(("disable", 0),
          ("fallback", 1),
          ("check", 2),
          ("secure", 3))
    )


_Qmode_Type.__name__ = "Integer32"
_Qmode_Object = MibTableColumn
qmode = _Qmode_Object(
    (1, 3, 6, 1, 4, 1, 12919, 4, 1, 1, 4),
    _Qmode_Type()
)
qmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qmode.setStatus("current")


class _DscpEnable_Type(Integer32):
    """Custom type dscpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DscpEnable_Type.__name__ = "Integer32"
_DscpEnable_Object = MibTableColumn
dscpEnable = _DscpEnable_Object(
    (1, 3, 6, 1, 4, 1, 12919, 4, 1, 1, 5),
    _DscpEnable_Type()
)
dscpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscpEnable.setStatus("current")
_VlangroupTable_Object = MibTable
vlangroupTable = _VlangroupTable_Object(
    (1, 3, 6, 1, 4, 1, 12919, 4, 2)
)
if mibBuilder.loadTexts:
    vlangroupTable.setStatus("current")
_GroupEntry_Object = MibTableRow
groupEntry = _GroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 12919, 4, 2, 1)
)
groupEntry.setIndexNames(
    (0, "XAVI-XG6846-MIB", "groupIndex"),
)
if mibBuilder.loadTexts:
    groupEntry.setStatus("current")
_GroupIndex_Type = Unsigned32
_GroupIndex_Object = MibTableColumn
groupIndex = _GroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 12919, 4, 2, 1, 1),
    _GroupIndex_Type()
)
groupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupIndex.setStatus("current")
_Groupid_Type = Unsigned32
_Groupid_Object = MibTableColumn
groupid = _Groupid_Object(
    (1, 3, 6, 1, 4, 1, 12919, 4, 2, 1, 2),
    _Groupid_Type()
)
groupid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupid.setStatus("current")


class _Lan1_Type(Integer32):
    """Custom type lan1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notMember", 0),
          ("egressUntagged", 1),
          ("egressTagged", 2))
    )


_Lan1_Type.__name__ = "Integer32"
_Lan1_Object = MibTableColumn
lan1 = _Lan1_Object(
    (1, 3, 6, 1, 4, 1, 12919, 4, 2, 1, 3),
    _Lan1_Type()
)
lan1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan1.setStatus("current")


class _Lan2_Type(Integer32):
    """Custom type lan2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notMember", 0),
          ("egressUntagged", 1),
          ("egressTagged", 2))
    )


_Lan2_Type.__name__ = "Integer32"
_Lan2_Object = MibTableColumn
lan2 = _Lan2_Object(
    (1, 3, 6, 1, 4, 1, 12919, 4, 2, 1, 4),
    _Lan2_Type()
)
lan2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan2.setStatus("current")


class _Lan3_Type(Integer32):
    """Custom type lan3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notMember", 0),
          ("egressUntagged", 1),
          ("egressTagged", 2))
    )


_Lan3_Type.__name__ = "Integer32"
_Lan3_Object = MibTableColumn
lan3 = _Lan3_Object(
    (1, 3, 6, 1, 4, 1, 12919, 4, 2, 1, 5),
    _Lan3_Type()
)
lan3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan3.setStatus("current")


class _Lan4_Type(Integer32):
    """Custom type lan4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notMember", 0),
          ("egressUntagged", 1),
          ("egressTagged", 2))
    )


_Lan4_Type.__name__ = "Integer32"
_Lan4_Object = MibTableColumn
lan4 = _Lan4_Object(
    (1, 3, 6, 1, 4, 1, 12919, 4, 2, 1, 6),
    _Lan4_Type()
)
lan4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan4.setStatus("current")


class _Wan_Type(Integer32):
    """Custom type wan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notMember", 0),
          ("egressUntagged", 1),
          ("egressTagged", 2))
    )


_Wan_Type.__name__ = "Integer32"
_Wan_Object = MibTableColumn
wan = _Wan_Object(
    (1, 3, 6, 1, 4, 1, 12919, 4, 2, 1, 7),
    _Wan_Type()
)
wan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wan.setStatus("current")
_PortStatistic_ObjectIdentity = ObjectIdentity
portStatistic = _PortStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12919, 5)
)
_StatisticTable_Object = MibTable
statisticTable = _StatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 12919, 5, 1)
)
if mibBuilder.loadTexts:
    statisticTable.setStatus("current")
_PortStatEntry_Object = MibTableRow
portStatEntry = _PortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 12919, 5, 1, 1)
)
portStatEntry.setIndexNames(
    (0, "XAVI-XG6846-MIB", "statIndex"),
)
if mibBuilder.loadTexts:
    portStatEntry.setStatus("current")
_StatIndex_Type = Unsigned32
_StatIndex_Object = MibTableColumn
statIndex = _StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 1),
    _StatIndex_Type()
)
statIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIndex.setStatus("current")
_PortName_Type = DisplayString
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 2),
    _PortName_Type()
)
portName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portName.setStatus("current")
_UnicastsReceived_Type = Unsigned32
_UnicastsReceived_Object = MibTableColumn
unicastsReceived = _UnicastsReceived_Object(
    (1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 3),
    _UnicastsReceived_Type()
)
unicastsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unicastsReceived.setStatus("current")
_BroadcastsReceived_Type = Unsigned32
_BroadcastsReceived_Object = MibTableColumn
broadcastsReceived = _BroadcastsReceived_Object(
    (1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 4),
    _BroadcastsReceived_Type()
)
broadcastsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    broadcastsReceived.setStatus("current")
_MulticastsReceived_Type = Unsigned32
_MulticastsReceived_Object = MibTableColumn
multicastsReceived = _MulticastsReceived_Object(
    (1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 5),
    _MulticastsReceived_Type()
)
multicastsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastsReceived.setStatus("current")
_FcsErrorReceived_Type = Unsigned32
_FcsErrorReceived_Object = MibTableColumn
fcsErrorReceived = _FcsErrorReceived_Object(
    (1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 6),
    _FcsErrorReceived_Type()
)
fcsErrorReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsErrorReceived.setStatus("current")
_PauseReceived_Type = Unsigned32
_PauseReceived_Object = MibTableColumn
pauseReceived = _PauseReceived_Object(
    (1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 7),
    _PauseReceived_Type()
)
pauseReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pauseReceived.setStatus("current")
_UnicastsTransmitted_Type = Unsigned32
_UnicastsTransmitted_Object = MibTableColumn
unicastsTransmitted = _UnicastsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 8),
    _UnicastsTransmitted_Type()
)
unicastsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unicastsTransmitted.setStatus("current")
_BroadcastsTransmitted_Type = Unsigned32
_BroadcastsTransmitted_Object = MibTableColumn
broadcastsTransmitted = _BroadcastsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 9),
    _BroadcastsTransmitted_Type()
)
broadcastsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    broadcastsTransmitted.setStatus("current")
_MulticastsTransmitted_Type = Unsigned32
_MulticastsTransmitted_Object = MibTableColumn
multicastsTransmitted = _MulticastsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 10),
    _MulticastsTransmitted_Type()
)
multicastsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastsTransmitted.setStatus("current")
_FcsErrorTransmitted_Type = Unsigned32
_FcsErrorTransmitted_Object = MibTableColumn
fcsErrorTransmitted = _FcsErrorTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 11),
    _FcsErrorTransmitted_Type()
)
fcsErrorTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsErrorTransmitted.setStatus("current")
_PauseTransmitted_Type = Unsigned32
_PauseTransmitted_Object = MibTableColumn
pauseTransmitted = _PauseTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 12),
    _PauseTransmitted_Type()
)
pauseTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pauseTransmitted.setStatus("current")
_Speed_Type = DisplayString
_Speed_Object = MibTableColumn
speed = _Speed_Object(
    (1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 13),
    _Speed_Type()
)
speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speed.setStatus("current")
_Ddminfo_ObjectIdentity = ObjectIdentity
ddminfo = _Ddminfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12919, 6)
)
_VendorName_Type = DisplayString
_VendorName_Object = MibScalar
vendorName = _VendorName_Object(
    (1, 3, 6, 1, 4, 1, 12919, 6, 1),
    _VendorName_Type()
)
vendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vendorName.setStatus("current")
_VendorOui_Type = DisplayString
_VendorOui_Object = MibScalar
vendorOui = _VendorOui_Object(
    (1, 3, 6, 1, 4, 1, 12919, 6, 2),
    _VendorOui_Type()
)
vendorOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vendorOui.setStatus("current")
_VendorPn_Type = DisplayString
_VendorPn_Object = MibScalar
vendorPn = _VendorPn_Object(
    (1, 3, 6, 1, 4, 1, 12919, 6, 3),
    _VendorPn_Type()
)
vendorPn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vendorPn.setStatus("current")
_VendorRev_Type = DisplayString
_VendorRev_Object = MibScalar
vendorRev = _VendorRev_Object(
    (1, 3, 6, 1, 4, 1, 12919, 6, 4),
    _VendorRev_Type()
)
vendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vendorRev.setStatus("current")
_Temperature_Type = DisplayString
_Temperature_Object = MibScalar
temperature = _Temperature_Object(
    (1, 3, 6, 1, 4, 1, 12919, 6, 5),
    _Temperature_Type()
)
temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature.setStatus("current")
_Voltage_Type = DisplayString
_Voltage_Object = MibScalar
voltage = _Voltage_Object(
    (1, 3, 6, 1, 4, 1, 12919, 6, 6),
    _Voltage_Type()
)
voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage.setStatus("current")
_Bias_Type = DisplayString
_Bias_Object = MibScalar
bias = _Bias_Object(
    (1, 3, 6, 1, 4, 1, 12919, 6, 7),
    _Bias_Type()
)
bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bias.setStatus("current")
_TxPower_Type = DisplayString
_TxPower_Object = MibScalar
txPower = _TxPower_Object(
    (1, 3, 6, 1, 4, 1, 12919, 6, 8),
    _TxPower_Type()
)
txPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txPower.setStatus("current")
_RxPower_Type = DisplayString
_RxPower_Object = MibScalar
rxPower = _RxPower_Object(
    (1, 3, 6, 1, 4, 1, 12919, 6, 9),
    _RxPower_Type()
)
rxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPower.setStatus("current")
_InternetPort_ObjectIdentity = ObjectIdentity
internetPort = _InternetPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12919, 7)
)


class _WanType_Type(Integer32):
    """Custom type wanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("staticIp", 2))
    )


_WanType_Type.__name__ = "Integer32"
_WanType_Object = MibScalar
wanType = _WanType_Object(
    (1, 3, 6, 1, 4, 1, 12919, 7, 1),
    _WanType_Type()
)
wanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanType.setStatus("current")
_Hostname_Type = DisplayString
_Hostname_Object = MibScalar
hostname = _Hostname_Object(
    (1, 3, 6, 1, 4, 1, 12919, 7, 2),
    _Hostname_Type()
)
hostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostname.setStatus("current")
_Domainame_Type = DisplayString
_Domainame_Object = MibScalar
domainame = _Domainame_Object(
    (1, 3, 6, 1, 4, 1, 12919, 7, 3),
    _Domainame_Type()
)
domainame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    domainame.setStatus("current")


class _StaticDns_Type(Integer32):
    """Custom type staticDns based on Integer32"""
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


_StaticDns_Type.__name__ = "Integer32"
_StaticDns_Object = MibScalar
staticDns = _StaticDns_Object(
    (1, 3, 6, 1, 4, 1, 12919, 7, 4),
    _StaticDns_Type()
)
staticDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticDns.setStatus("current")
_PrimaryDns_Type = DisplayString
_PrimaryDns_Object = MibScalar
primaryDns = _PrimaryDns_Object(
    (1, 3, 6, 1, 4, 1, 12919, 7, 5),
    _PrimaryDns_Type()
)
primaryDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryDns.setStatus("current")
_SecondaryDns_Type = DisplayString
_SecondaryDns_Object = MibScalar
secondaryDns = _SecondaryDns_Object(
    (1, 3, 6, 1, 4, 1, 12919, 7, 6),
    _SecondaryDns_Type()
)
secondaryDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondaryDns.setStatus("current")
_StaticIpHostName_Type = DisplayString
_StaticIpHostName_Object = MibScalar
staticIpHostName = _StaticIpHostName_Object(
    (1, 3, 6, 1, 4, 1, 12919, 7, 7),
    _StaticIpHostName_Type()
)
staticIpHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticIpHostName.setStatus("current")
_StaticIpDomainName_Type = DisplayString
_StaticIpDomainName_Object = MibScalar
staticIpDomainName = _StaticIpDomainName_Object(
    (1, 3, 6, 1, 4, 1, 12919, 7, 8),
    _StaticIpDomainName_Type()
)
staticIpDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticIpDomainName.setStatus("current")
_StaticIpAddr_Type = DisplayString
_StaticIpAddr_Object = MibScalar
staticIpAddr = _StaticIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 12919, 7, 9),
    _StaticIpAddr_Type()
)
staticIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticIpAddr.setStatus("current")
_StaticIpSubMask_Type = DisplayString
_StaticIpSubMask_Object = MibScalar
staticIpSubMask = _StaticIpSubMask_Object(
    (1, 3, 6, 1, 4, 1, 12919, 7, 10),
    _StaticIpSubMask_Type()
)
staticIpSubMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticIpSubMask.setStatus("current")
_StaticIpGateway_Type = DisplayString
_StaticIpGateway_Object = MibScalar
staticIpGateway = _StaticIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 12919, 7, 11),
    _StaticIpGateway_Type()
)
staticIpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticIpGateway.setStatus("current")
_StaticIpPrimaryDns_Type = DisplayString
_StaticIpPrimaryDns_Object = MibScalar
staticIpPrimaryDns = _StaticIpPrimaryDns_Object(
    (1, 3, 6, 1, 4, 1, 12919, 7, 12),
    _StaticIpPrimaryDns_Type()
)
staticIpPrimaryDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticIpPrimaryDns.setStatus("current")
_StaticIpSecondaryDns_Type = DisplayString
_StaticIpSecondaryDns_Object = MibScalar
staticIpSecondaryDns = _StaticIpSecondaryDns_Object(
    (1, 3, 6, 1, 4, 1, 12919, 7, 13),
    _StaticIpSecondaryDns_Type()
)
staticIpSecondaryDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticIpSecondaryDns.setStatus("current")
_Reboot_ObjectIdentity = ObjectIdentity
reboot = _Reboot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12919, 8)
)


class _RebootEnable_Type(Integer32):
    """Custom type rebootEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RebootEnable_Type.__name__ = "Integer32"
_RebootEnable_Object = MibScalar
rebootEnable = _RebootEnable_Object(
    (1, 3, 6, 1, 4, 1, 12919, 8, 1),
    _RebootEnable_Type()
)
rebootEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rebootEnable.setStatus("current")
_Tftp_ObjectIdentity = ObjectIdentity
tftp = _Tftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12919, 9)
)
_TftpSevIp_Type = IpAddress
_TftpSevIp_Object = MibScalar
tftpSevIp = _TftpSevIp_Object(
    (1, 3, 6, 1, 4, 1, 12919, 9, 1),
    _TftpSevIp_Type()
)
tftpSevIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpSevIp.setStatus("current")
_FileName_Type = DisplayString
_FileName_Object = MibScalar
fileName = _FileName_Object(
    (1, 3, 6, 1, 4, 1, 12919, 9, 2),
    _FileName_Type()
)
fileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileName.setStatus("current")
_FileType_Type = DisplayString
_FileType_Object = MibScalar
fileType = _FileType_Object(
    (1, 3, 6, 1, 4, 1, 12919, 9, 3),
    _FileType_Type()
)
fileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileType.setStatus("current")
_Action_Type = DisplayString
_Action_Object = MibScalar
action = _Action_Object(
    (1, 3, 6, 1, 4, 1, 12919, 9, 4),
    _Action_Type()
)
action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    action.setStatus("current")


class _AdminStatus_Type(Integer32):
    """Custom type adminStatus based on Integer32"""
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


_AdminStatus_Type.__name__ = "Integer32"
_AdminStatus_Object = MibScalar
adminStatus = _AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 12919, 9, 5),
    _AdminStatus_Type()
)
adminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminStatus.setStatus("current")


class _OperStatus_Type(Integer32):
    """Custom type operStatus based on Integer32"""
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


_OperStatus_Type.__name__ = "Integer32"
_OperStatus_Object = MibScalar
operStatus = _OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 12919, 9, 6),
    _OperStatus_Type()
)
operStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operStatus.setStatus("current")
_PortPower_ObjectIdentity = ObjectIdentity
portPower = _PortPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12919, 10)
)


class _Port1_Type(Integer32):
    """Custom type port1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Port1_Type.__name__ = "Integer32"
_Port1_Object = MibScalar
port1 = _Port1_Object(
    (1, 3, 6, 1, 4, 1, 12919, 10, 1),
    _Port1_Type()
)
port1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port1.setStatus("current")


class _Port2_Type(Integer32):
    """Custom type port2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Port2_Type.__name__ = "Integer32"
_Port2_Object = MibScalar
port2 = _Port2_Object(
    (1, 3, 6, 1, 4, 1, 12919, 10, 2),
    _Port2_Type()
)
port2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port2.setStatus("current")


class _Port3_Type(Integer32):
    """Custom type port3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Port3_Type.__name__ = "Integer32"
_Port3_Object = MibScalar
port3 = _Port3_Object(
    (1, 3, 6, 1, 4, 1, 12919, 10, 3),
    _Port3_Type()
)
port3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port3.setStatus("current")


class _Port4_Type(Integer32):
    """Custom type port4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Port4_Type.__name__ = "Integer32"
_Port4_Object = MibScalar
port4 = _Port4_Object(
    (1, 3, 6, 1, 4, 1, 12919, 10, 4),
    _Port4_Type()
)
port4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port4.setStatus("current")
_Jumb_ObjectIdentity = ObjectIdentity
jumb = _Jumb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12919, 11)
)


class _Jumblan1_Type(Integer32):
    """Custom type jumblan1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode1", 0),
          ("mode2", 1),
          ("mode3", 2))
    )


_Jumblan1_Type.__name__ = "Integer32"
_Jumblan1_Object = MibScalar
jumblan1 = _Jumblan1_Object(
    (1, 3, 6, 1, 4, 1, 12919, 11, 1),
    _Jumblan1_Type()
)
jumblan1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jumblan1.setStatus("current")


class _Jumblan2_Type(Integer32):
    """Custom type jumblan2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode1", 0),
          ("mode2", 1),
          ("mode3", 2))
    )


_Jumblan2_Type.__name__ = "Integer32"
_Jumblan2_Object = MibScalar
jumblan2 = _Jumblan2_Object(
    (1, 3, 6, 1, 4, 1, 12919, 11, 2),
    _Jumblan2_Type()
)
jumblan2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jumblan2.setStatus("current")


class _Jumblan3_Type(Integer32):
    """Custom type jumblan3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode1", 0),
          ("mode2", 1),
          ("mode3", 2))
    )


_Jumblan3_Type.__name__ = "Integer32"
_Jumblan3_Object = MibScalar
jumblan3 = _Jumblan3_Object(
    (1, 3, 6, 1, 4, 1, 12919, 11, 3),
    _Jumblan3_Type()
)
jumblan3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jumblan3.setStatus("current")


class _Jumblan4_Type(Integer32):
    """Custom type jumblan4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode1", 0),
          ("mode2", 1),
          ("mode3", 2))
    )


_Jumblan4_Type.__name__ = "Integer32"
_Jumblan4_Object = MibScalar
jumblan4 = _Jumblan4_Object(
    (1, 3, 6, 1, 4, 1, 12919, 11, 4),
    _Jumblan4_Type()
)
jumblan4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jumblan4.setStatus("current")


class _Jumbwan_Type(Integer32):
    """Custom type jumbwan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode1", 0),
          ("mode2", 1),
          ("mode3", 2))
    )


_Jumbwan_Type.__name__ = "Integer32"
_Jumbwan_Object = MibScalar
jumbwan = _Jumbwan_Object(
    (1, 3, 6, 1, 4, 1, 12919, 11, 5),
    _Jumbwan_Type()
)
jumbwan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jumbwan.setStatus("current")
_Deviceinfo_ObjectIdentity = ObjectIdentity
deviceinfo = _Deviceinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12919, 12)
)
_Serialnum_Type = DisplayString
_Serialnum_Object = MibScalar
serialnum = _Serialnum_Object(
    (1, 3, 6, 1, 4, 1, 12919, 12, 1),
    _Serialnum_Type()
)
serialnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialnum.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XAVI-XG6846-MIB",
    **{"xg6846": xg6846,
       "catv": catv,
       "catvEnable": catvEnable,
       "portmode": portmode,
       "lanportTable": lanportTable,
       "modeEntry": modeEntry,
       "lanportIndex": lanportIndex,
       "lanportName": lanportName,
       "lanportspeed": lanportspeed,
       "lanportpause": lanportpause,
       "qos": qos,
       "qosTable": qosTable,
       "qosEntry": qosEntry,
       "qosIndex": qosIndex,
       "qmapping": qmapping,
       "vlan": vlan,
       "portTable": portTable,
       "portEntry": portEntry,
       "portIndex": portIndex,
       "vlanid": vlanid,
       "priority": priority,
       "qmode": qmode,
       "dscpEnable": dscpEnable,
       "vlangroupTable": vlangroupTable,
       "groupEntry": groupEntry,
       "groupIndex": groupIndex,
       "groupid": groupid,
       "lan1": lan1,
       "lan2": lan2,
       "lan3": lan3,
       "lan4": lan4,
       "wan": wan,
       "portStatistic": portStatistic,
       "statisticTable": statisticTable,
       "portStatEntry": portStatEntry,
       "statIndex": statIndex,
       "portName": portName,
       "unicastsReceived": unicastsReceived,
       "broadcastsReceived": broadcastsReceived,
       "multicastsReceived": multicastsReceived,
       "fcsErrorReceived": fcsErrorReceived,
       "pauseReceived": pauseReceived,
       "unicastsTransmitted": unicastsTransmitted,
       "broadcastsTransmitted": broadcastsTransmitted,
       "multicastsTransmitted": multicastsTransmitted,
       "fcsErrorTransmitted": fcsErrorTransmitted,
       "pauseTransmitted": pauseTransmitted,
       "speed": speed,
       "ddminfo": ddminfo,
       "vendorName": vendorName,
       "vendorOui": vendorOui,
       "vendorPn": vendorPn,
       "vendorRev": vendorRev,
       "temperature": temperature,
       "voltage": voltage,
       "bias": bias,
       "txPower": txPower,
       "rxPower": rxPower,
       "internetPort": internetPort,
       "wanType": wanType,
       "hostname": hostname,
       "domainame": domainame,
       "staticDns": staticDns,
       "primaryDns": primaryDns,
       "secondaryDns": secondaryDns,
       "staticIpHostName": staticIpHostName,
       "staticIpDomainName": staticIpDomainName,
       "staticIpAddr": staticIpAddr,
       "staticIpSubMask": staticIpSubMask,
       "staticIpGateway": staticIpGateway,
       "staticIpPrimaryDns": staticIpPrimaryDns,
       "staticIpSecondaryDns": staticIpSecondaryDns,
       "reboot": reboot,
       "rebootEnable": rebootEnable,
       "tftp": tftp,
       "tftpSevIp": tftpSevIp,
       "fileName": fileName,
       "fileType": fileType,
       "action": action,
       "adminStatus": adminStatus,
       "operStatus": operStatus,
       "portPower": portPower,
       "port1": port1,
       "port2": port2,
       "port3": port3,
       "port4": port4,
       "jumb": jumb,
       "jumblan1": jumblan1,
       "jumblan2": jumblan2,
       "jumblan3": jumblan3,
       "jumblan4": jumblan4,
       "jumbwan": jumbwan,
       "deviceinfo": deviceinfo,
       "serialnum": serialnum}
)
