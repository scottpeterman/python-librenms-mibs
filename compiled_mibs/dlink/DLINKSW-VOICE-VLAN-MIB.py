# SNMP MIB module (DLINKSW-VOICE-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-VOICE-VLAN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:38:09 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(LldpChassisId,
 LldpChassisIdSubtype,
 LldpPortId,
 LldpPortIdSubtype,
 LldpPortNumber) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "LldpChassisId",
    "LldpChassisIdSubtype",
    "LldpPortId",
    "LldpPortIdSubtype",
    "LldpPortNumber")

(PortList,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIdOrNone")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwVoiceVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 74)
)
if mibBuilder.loadTexts:
    dlinkSwVoiceVlanMIB.setRevisions(
        ("2013-04-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DVoiceVlanMIBNotifications_ObjectIdentity = ObjectIdentity
dVoiceVlanMIBNotifications = _DVoiceVlanMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 0)
)
_DVoiceVlanMIBObjects_ObjectIdentity = ObjectIdentity
dVoiceVlanMIBObjects = _DVoiceVlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1)
)
_DVoiceVlanGlobal_ObjectIdentity = ObjectIdentity
dVoiceVlanGlobal = _DVoiceVlanGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 1)
)


class _DVoiceVlanVlanId_Type(VlanIdOrNone):
    """Custom type dVoiceVlanVlanId based on VlanIdOrNone"""
    defaultValue = 0


_DVoiceVlanVlanId_Type.__name__ = "VlanIdOrNone"
_DVoiceVlanVlanId_Object = MibScalar
dVoiceVlanVlanId = _DVoiceVlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 1, 1),
    _DVoiceVlanVlanId_Type()
)
dVoiceVlanVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dVoiceVlanVlanId.setStatus("current")


class _DVoiceVlanQos_Type(Unsigned32):
    """Custom type dVoiceVlanQos based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DVoiceVlanQos_Type.__name__ = "Unsigned32"
_DVoiceVlanQos_Object = MibScalar
dVoiceVlanQos = _DVoiceVlanQos_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 1, 2),
    _DVoiceVlanQos_Type()
)
dVoiceVlanQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dVoiceVlanQos.setStatus("current")


class _DVoiceVlanAgingTime_Type(Unsigned32):
    """Custom type dVoiceVlanAgingTime based on Unsigned32"""
    defaultValue = 720

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DVoiceVlanAgingTime_Type.__name__ = "Unsigned32"
_DVoiceVlanAgingTime_Object = MibScalar
dVoiceVlanAgingTime = _DVoiceVlanAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 1, 3),
    _DVoiceVlanAgingTime_Type()
)
dVoiceVlanAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dVoiceVlanAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    dVoiceVlanAgingTime.setUnits("minutes")
_DVoiceVlanOuiTable_Object = MibTable
dVoiceVlanOuiTable = _DVoiceVlanOuiTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 1, 4)
)
if mibBuilder.loadTexts:
    dVoiceVlanOuiTable.setStatus("current")
_DVoiceVlanOuiEntry_Object = MibTableRow
dVoiceVlanOuiEntry = _DVoiceVlanOuiEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 1, 4, 1)
)
dVoiceVlanOuiEntry.setIndexNames(
    (0, "DLINKSW-VOICE-VLAN-MIB", "dVoiceVlanOuiAddr"),
    (0, "DLINKSW-VOICE-VLAN-MIB", "dVoiceVlanOuiMask"),
)
if mibBuilder.loadTexts:
    dVoiceVlanOuiEntry.setStatus("current")
_DVoiceVlanOuiAddr_Type = MacAddress
_DVoiceVlanOuiAddr_Object = MibTableColumn
dVoiceVlanOuiAddr = _DVoiceVlanOuiAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 1, 4, 1, 1),
    _DVoiceVlanOuiAddr_Type()
)
dVoiceVlanOuiAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dVoiceVlanOuiAddr.setStatus("current")
_DVoiceVlanOuiMask_Type = MacAddress
_DVoiceVlanOuiMask_Object = MibTableColumn
dVoiceVlanOuiMask = _DVoiceVlanOuiMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 1, 4, 1, 2),
    _DVoiceVlanOuiMask_Type()
)
dVoiceVlanOuiMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dVoiceVlanOuiMask.setStatus("current")


class _DVoiceVlanOuiDes_Type(SnmpAdminString):
    """Custom type dVoiceVlanOuiDes based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DVoiceVlanOuiDes_Type.__name__ = "SnmpAdminString"
_DVoiceVlanOuiDes_Object = MibTableColumn
dVoiceVlanOuiDes = _DVoiceVlanOuiDes_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 1, 4, 1, 3),
    _DVoiceVlanOuiDes_Type()
)
dVoiceVlanOuiDes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dVoiceVlanOuiDes.setStatus("current")
_DVoiceVlanOuiRowStatus_Type = RowStatus
_DVoiceVlanOuiRowStatus_Object = MibTableColumn
dVoiceVlanOuiRowStatus = _DVoiceVlanOuiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 1, 4, 1, 4),
    _DVoiceVlanOuiRowStatus_Type()
)
dVoiceVlanOuiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dVoiceVlanOuiRowStatus.setStatus("current")
_DVoiceVlanInterface_ObjectIdentity = ObjectIdentity
dVoiceVlanInterface = _DVoiceVlanInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 2)
)
_DVoiceVlanInterfaceTable_Object = MibTable
dVoiceVlanInterfaceTable = _DVoiceVlanInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dVoiceVlanInterfaceTable.setStatus("current")
_DVoiceVlanInterfaceEntry_Object = MibTableRow
dVoiceVlanInterfaceEntry = _DVoiceVlanInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 2, 1, 1)
)
dVoiceVlanInterfaceEntry.setIndexNames(
    (0, "DLINKSW-VOICE-VLAN-MIB", "dVoiceVlanIfIndex"),
)
if mibBuilder.loadTexts:
    dVoiceVlanInterfaceEntry.setStatus("current")
_DVoiceVlanIfIndex_Type = InterfaceIndex
_DVoiceVlanIfIndex_Object = MibTableColumn
dVoiceVlanIfIndex = _DVoiceVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 2, 1, 1, 1),
    _DVoiceVlanIfIndex_Type()
)
dVoiceVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dVoiceVlanIfIndex.setStatus("current")
_DVoiceVlanIfEnabled_Type = TruthValue
_DVoiceVlanIfEnabled_Object = MibTableColumn
dVoiceVlanIfEnabled = _DVoiceVlanIfEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 2, 1, 1, 2),
    _DVoiceVlanIfEnabled_Type()
)
dVoiceVlanIfEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dVoiceVlanIfEnabled.setStatus("current")


class _DVoiceVlanIfMode_Type(Integer32):
    """Custom type dVoiceVlanIfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoUntagged", 1),
          ("autoTagged", 2),
          ("manual", 3))
    )


_DVoiceVlanIfMode_Type.__name__ = "Integer32"
_DVoiceVlanIfMode_Object = MibTableColumn
dVoiceVlanIfMode = _DVoiceVlanIfMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 2, 1, 1, 3),
    _DVoiceVlanIfMode_Type()
)
dVoiceVlanIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dVoiceVlanIfMode.setStatus("current")
_DVoiceVlanInfo_ObjectIdentity = ObjectIdentity
dVoiceVlanInfo = _DVoiceVlanInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 3)
)
_DVoiceVlanMemberPorts_Type = PortList
_DVoiceVlanMemberPorts_Object = MibScalar
dVoiceVlanMemberPorts = _DVoiceVlanMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 3, 1),
    _DVoiceVlanMemberPorts_Type()
)
dVoiceVlanMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dVoiceVlanMemberPorts.setStatus("current")
_DVoiceVlanDynamicMemberPorts_Type = PortList
_DVoiceVlanDynamicMemberPorts_Object = MibScalar
dVoiceVlanDynamicMemberPorts = _DVoiceVlanDynamicMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 3, 2),
    _DVoiceVlanDynamicMemberPorts_Type()
)
dVoiceVlanDynamicMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dVoiceVlanDynamicMemberPorts.setStatus("current")
_DVoiceVlanDeviceTable_Object = MibTable
dVoiceVlanDeviceTable = _DVoiceVlanDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 3, 3)
)
if mibBuilder.loadTexts:
    dVoiceVlanDeviceTable.setStatus("current")
_DVoiceVlanDeviceEntry_Object = MibTableRow
dVoiceVlanDeviceEntry = _DVoiceVlanDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 3, 3, 1)
)
dVoiceVlanDeviceEntry.setIndexNames(
    (0, "DLINKSW-VOICE-VLAN-MIB", "dVoiceVlanDevicePortIfindex"),
    (0, "DLINKSW-VOICE-VLAN-MIB", "dVoiceVlanDeviceAddr"),
)
if mibBuilder.loadTexts:
    dVoiceVlanDeviceEntry.setStatus("current")
_DVoiceVlanDevicePortIfindex_Type = InterfaceIndex
_DVoiceVlanDevicePortIfindex_Object = MibTableColumn
dVoiceVlanDevicePortIfindex = _DVoiceVlanDevicePortIfindex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 3, 3, 1, 1),
    _DVoiceVlanDevicePortIfindex_Type()
)
dVoiceVlanDevicePortIfindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dVoiceVlanDevicePortIfindex.setStatus("current")
_DVoiceVlanDeviceAddr_Type = MacAddress
_DVoiceVlanDeviceAddr_Object = MibTableColumn
dVoiceVlanDeviceAddr = _DVoiceVlanDeviceAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 3, 3, 1, 2),
    _DVoiceVlanDeviceAddr_Type()
)
dVoiceVlanDeviceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dVoiceVlanDeviceAddr.setStatus("current")
_DVoiceVlanDeviceStartTime_Type = DateAndTime
_DVoiceVlanDeviceStartTime_Object = MibTableColumn
dVoiceVlanDeviceStartTime = _DVoiceVlanDeviceStartTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 3, 3, 1, 3),
    _DVoiceVlanDeviceStartTime_Type()
)
dVoiceVlanDeviceStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dVoiceVlanDeviceStartTime.setStatus("current")


class _DVoiceVlanDeviceStatus_Type(Integer32):
    """Custom type dVoiceVlanDeviceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("aging", 2))
    )


_DVoiceVlanDeviceStatus_Type.__name__ = "Integer32"
_DVoiceVlanDeviceStatus_Object = MibTableColumn
dVoiceVlanDeviceStatus = _DVoiceVlanDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 3, 3, 1, 4),
    _DVoiceVlanDeviceStatus_Type()
)
dVoiceVlanDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dVoiceVlanDeviceStatus.setStatus("current")
_DVoiceVlanLldpMedDeviceTable_Object = MibTable
dVoiceVlanLldpMedDeviceTable = _DVoiceVlanLldpMedDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 3, 4)
)
if mibBuilder.loadTexts:
    dVoiceVlanLldpMedDeviceTable.setStatus("current")
_DVoiceVlanLldpMedDeviceEntry_Object = MibTableRow
dVoiceVlanLldpMedDeviceEntry = _DVoiceVlanLldpMedDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 3, 4, 1)
)
dVoiceVlanLldpMedDeviceEntry.setIndexNames(
    (0, "DLINKSW-VOICE-VLAN-MIB", "dVoiceVlanLldpMedDeviceIndex"),
)
if mibBuilder.loadTexts:
    dVoiceVlanLldpMedDeviceEntry.setStatus("current")


class _DVoiceVlanLldpMedDeviceIndex_Type(Unsigned32):
    """Custom type dVoiceVlanLldpMedDeviceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DVoiceVlanLldpMedDeviceIndex_Type.__name__ = "Unsigned32"
_DVoiceVlanLldpMedDeviceIndex_Object = MibTableColumn
dVoiceVlanLldpMedDeviceIndex = _DVoiceVlanLldpMedDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 3, 4, 1, 1),
    _DVoiceVlanLldpMedDeviceIndex_Type()
)
dVoiceVlanLldpMedDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dVoiceVlanLldpMedDeviceIndex.setStatus("current")
_DVoiceVlanLldpMedDeviceLocalPort_Type = LldpPortNumber
_DVoiceVlanLldpMedDeviceLocalPort_Object = MibTableColumn
dVoiceVlanLldpMedDeviceLocalPort = _DVoiceVlanLldpMedDeviceLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 3, 4, 1, 2),
    _DVoiceVlanLldpMedDeviceLocalPort_Type()
)
dVoiceVlanLldpMedDeviceLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dVoiceVlanLldpMedDeviceLocalPort.setStatus("current")
_DVoiceVlanLldpMedDevChIdSubtype_Type = LldpChassisIdSubtype
_DVoiceVlanLldpMedDevChIdSubtype_Object = MibTableColumn
dVoiceVlanLldpMedDevChIdSubtype = _DVoiceVlanLldpMedDevChIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 3, 4, 1, 3),
    _DVoiceVlanLldpMedDevChIdSubtype_Type()
)
dVoiceVlanLldpMedDevChIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dVoiceVlanLldpMedDevChIdSubtype.setStatus("current")
_DVoiceVlanLldpMedDevChassisId_Type = LldpChassisId
_DVoiceVlanLldpMedDevChassisId_Object = MibTableColumn
dVoiceVlanLldpMedDevChassisId = _DVoiceVlanLldpMedDevChassisId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 3, 4, 1, 4),
    _DVoiceVlanLldpMedDevChassisId_Type()
)
dVoiceVlanLldpMedDevChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dVoiceVlanLldpMedDevChassisId.setStatus("current")
_DVoiceVlanLldpMedDevPoIdSubtype_Type = LldpPortIdSubtype
_DVoiceVlanLldpMedDevPoIdSubtype_Object = MibTableColumn
dVoiceVlanLldpMedDevPoIdSubtype = _DVoiceVlanLldpMedDevPoIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 3, 4, 1, 5),
    _DVoiceVlanLldpMedDevPoIdSubtype_Type()
)
dVoiceVlanLldpMedDevPoIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dVoiceVlanLldpMedDevPoIdSubtype.setStatus("current")
_DVoiceVlanLldpMedDevicePortId_Type = LldpPortId
_DVoiceVlanLldpMedDevicePortId_Object = MibTableColumn
dVoiceVlanLldpMedDevicePortId = _DVoiceVlanLldpMedDevicePortId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 3, 4, 1, 6),
    _DVoiceVlanLldpMedDevicePortId_Type()
)
dVoiceVlanLldpMedDevicePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dVoiceVlanLldpMedDevicePortId.setStatus("current")
_DVoiceVlanLldpMedDevCreateTime_Type = DateAndTime
_DVoiceVlanLldpMedDevCreateTime_Object = MibTableColumn
dVoiceVlanLldpMedDevCreateTime = _DVoiceVlanLldpMedDevCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 3, 4, 1, 7),
    _DVoiceVlanLldpMedDevCreateTime_Type()
)
dVoiceVlanLldpMedDevCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dVoiceVlanLldpMedDevCreateTime.setStatus("current")
_DVoiceVlanLldpMedDevRemainTime_Type = Unsigned32
_DVoiceVlanLldpMedDevRemainTime_Object = MibTableColumn
dVoiceVlanLldpMedDevRemainTime = _DVoiceVlanLldpMedDevRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 1, 3, 4, 1, 8),
    _DVoiceVlanLldpMedDevRemainTime_Type()
)
dVoiceVlanLldpMedDevRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dVoiceVlanLldpMedDevRemainTime.setStatus("current")
if mibBuilder.loadTexts:
    dVoiceVlanLldpMedDevRemainTime.setUnits("seconds")
_DVoiceVlanMIBConformance_ObjectIdentity = ObjectIdentity
dVoiceVlanMIBConformance = _DVoiceVlanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 2)
)
_DVoiceVlanMIBCompliances_ObjectIdentity = ObjectIdentity
dVoiceVlanMIBCompliances = _DVoiceVlanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 2, 1)
)
_DVoiceVlanMIBGroups_ObjectIdentity = ObjectIdentity
dVoiceVlanMIBGroups = _DVoiceVlanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 2, 2)
)

# Managed Objects groups

dVoiceVlanBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 2, 2, 1)
)
dVoiceVlanBasicGroup.setObjects(
      *(("DLINKSW-VOICE-VLAN-MIB", "dVoiceVlanVlanId"),
        ("DLINKSW-VOICE-VLAN-MIB", "dVoiceVlanQos"),
        ("DLINKSW-VOICE-VLAN-MIB", "dVoiceVlanAgingTime"),
        ("DLINKSW-VOICE-VLAN-MIB", "dVoiceVlanIfEnabled"),
        ("DLINKSW-VOICE-VLAN-MIB", "dVoiceVlanIfMode"),
        ("DLINKSW-VOICE-VLAN-MIB", "dVoiceVlanMemberPorts"),
        ("DLINKSW-VOICE-VLAN-MIB", "dVoiceVlanDynamicMemberPorts"))
)
if mibBuilder.loadTexts:
    dVoiceVlanBasicGroup.setStatus("current")

dVoiceVlanOUICfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 2, 2, 2)
)
dVoiceVlanOUICfgGroup.setObjects(
      *(("DLINKSW-VOICE-VLAN-MIB", "dVoiceVlanOuiDes"),
        ("DLINKSW-VOICE-VLAN-MIB", "dVoiceVlanOuiRowStatus"))
)
if mibBuilder.loadTexts:
    dVoiceVlanOUICfgGroup.setStatus("current")

dVoiceVlanDeviceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 2, 2, 3)
)
dVoiceVlanDeviceInfoGroup.setObjects(
      *(("DLINKSW-VOICE-VLAN-MIB", "dVoiceVlanDeviceStartTime"),
        ("DLINKSW-VOICE-VLAN-MIB", "dVoiceVlanDeviceStatus"))
)
if mibBuilder.loadTexts:
    dVoiceVlanDeviceInfoGroup.setStatus("current")

dVoiceVlanDeviceLldpMedInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 2, 2, 4)
)
dVoiceVlanDeviceLldpMedInfoGroup.setObjects(
      *(("DLINKSW-VOICE-VLAN-MIB", "dVoiceVlanLldpMedDeviceLocalPort"),
        ("DLINKSW-VOICE-VLAN-MIB", "dVoiceVlanLldpMedDevChIdSubtype"),
        ("DLINKSW-VOICE-VLAN-MIB", "dVoiceVlanLldpMedDevChassisId"),
        ("DLINKSW-VOICE-VLAN-MIB", "dVoiceVlanLldpMedDevPoIdSubtype"),
        ("DLINKSW-VOICE-VLAN-MIB", "dVoiceVlanLldpMedDevicePortId"),
        ("DLINKSW-VOICE-VLAN-MIB", "dVoiceVlanLldpMedDevCreateTime"),
        ("DLINKSW-VOICE-VLAN-MIB", "dVoiceVlanLldpMedDevRemainTime"))
)
if mibBuilder.loadTexts:
    dVoiceVlanDeviceLldpMedInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dVoiceVlanMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 74, 2, 1, 1)
)
dVoiceVlanMIBCompliance.setObjects(
      *(("DLINKSW-VOICE-VLAN-MIB", "dVoiceVlanBasicGroup"),
        ("DLINKSW-VOICE-VLAN-MIB", "dVoiceVlanOUICfgGroup"),
        ("DLINKSW-VOICE-VLAN-MIB", "dVoiceVlanDeviceInfoGroup"),
        ("DLINKSW-VOICE-VLAN-MIB", "dVoiceVlanDeviceLldpMedInfoGroup"))
)
if mibBuilder.loadTexts:
    dVoiceVlanMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-VOICE-VLAN-MIB",
    **{"dlinkSwVoiceVlanMIB": dlinkSwVoiceVlanMIB,
       "dVoiceVlanMIBNotifications": dVoiceVlanMIBNotifications,
       "dVoiceVlanMIBObjects": dVoiceVlanMIBObjects,
       "dVoiceVlanGlobal": dVoiceVlanGlobal,
       "dVoiceVlanVlanId": dVoiceVlanVlanId,
       "dVoiceVlanQos": dVoiceVlanQos,
       "dVoiceVlanAgingTime": dVoiceVlanAgingTime,
       "dVoiceVlanOuiTable": dVoiceVlanOuiTable,
       "dVoiceVlanOuiEntry": dVoiceVlanOuiEntry,
       "dVoiceVlanOuiAddr": dVoiceVlanOuiAddr,
       "dVoiceVlanOuiMask": dVoiceVlanOuiMask,
       "dVoiceVlanOuiDes": dVoiceVlanOuiDes,
       "dVoiceVlanOuiRowStatus": dVoiceVlanOuiRowStatus,
       "dVoiceVlanInterface": dVoiceVlanInterface,
       "dVoiceVlanInterfaceTable": dVoiceVlanInterfaceTable,
       "dVoiceVlanInterfaceEntry": dVoiceVlanInterfaceEntry,
       "dVoiceVlanIfIndex": dVoiceVlanIfIndex,
       "dVoiceVlanIfEnabled": dVoiceVlanIfEnabled,
       "dVoiceVlanIfMode": dVoiceVlanIfMode,
       "dVoiceVlanInfo": dVoiceVlanInfo,
       "dVoiceVlanMemberPorts": dVoiceVlanMemberPorts,
       "dVoiceVlanDynamicMemberPorts": dVoiceVlanDynamicMemberPorts,
       "dVoiceVlanDeviceTable": dVoiceVlanDeviceTable,
       "dVoiceVlanDeviceEntry": dVoiceVlanDeviceEntry,
       "dVoiceVlanDevicePortIfindex": dVoiceVlanDevicePortIfindex,
       "dVoiceVlanDeviceAddr": dVoiceVlanDeviceAddr,
       "dVoiceVlanDeviceStartTime": dVoiceVlanDeviceStartTime,
       "dVoiceVlanDeviceStatus": dVoiceVlanDeviceStatus,
       "dVoiceVlanLldpMedDeviceTable": dVoiceVlanLldpMedDeviceTable,
       "dVoiceVlanLldpMedDeviceEntry": dVoiceVlanLldpMedDeviceEntry,
       "dVoiceVlanLldpMedDeviceIndex": dVoiceVlanLldpMedDeviceIndex,
       "dVoiceVlanLldpMedDeviceLocalPort": dVoiceVlanLldpMedDeviceLocalPort,
       "dVoiceVlanLldpMedDevChIdSubtype": dVoiceVlanLldpMedDevChIdSubtype,
       "dVoiceVlanLldpMedDevChassisId": dVoiceVlanLldpMedDevChassisId,
       "dVoiceVlanLldpMedDevPoIdSubtype": dVoiceVlanLldpMedDevPoIdSubtype,
       "dVoiceVlanLldpMedDevicePortId": dVoiceVlanLldpMedDevicePortId,
       "dVoiceVlanLldpMedDevCreateTime": dVoiceVlanLldpMedDevCreateTime,
       "dVoiceVlanLldpMedDevRemainTime": dVoiceVlanLldpMedDevRemainTime,
       "dVoiceVlanMIBConformance": dVoiceVlanMIBConformance,
       "dVoiceVlanMIBCompliances": dVoiceVlanMIBCompliances,
       "dVoiceVlanMIBCompliance": dVoiceVlanMIBCompliance,
       "dVoiceVlanMIBGroups": dVoiceVlanMIBGroups,
       "dVoiceVlanBasicGroup": dVoiceVlanBasicGroup,
       "dVoiceVlanOUICfgGroup": dVoiceVlanOUICfgGroup,
       "dVoiceVlanDeviceInfoGroup": dVoiceVlanDeviceInfoGroup,
       "dVoiceVlanDeviceLldpMedInfoGroup": dVoiceVlanDeviceLldpMedInfoGroup}
)
