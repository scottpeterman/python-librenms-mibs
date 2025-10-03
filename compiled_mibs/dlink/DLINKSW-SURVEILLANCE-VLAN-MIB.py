# SNMP MIB module (DLINKSW-SURVEILLANCE-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-SURVEILLANCE-VLAN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:56 2025
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

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

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

dlinkSwSurveillanceVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 34)
)
if mibBuilder.loadTexts:
    dlinkSwSurveillanceVlanMIB.setRevisions(
        ("2013-04-08 00:00",
         "2016-03-28 00:00",
         "2016-10-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class OuiComponentType(TextualConvention, Integer32):
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
        *(("other", 1),
          ("dlink", 2),
          ("vms", 3),
          ("vmsClient", 4),
          ("videoEncoder", 5),
          ("networkStorage", 6))
    )



# MIB Managed Objects in the order of their OIDs

_DsvMIBNotifications_ObjectIdentity = ObjectIdentity
dsvMIBNotifications = _DsvMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 0)
)
_DsvMIBObjects_ObjectIdentity = ObjectIdentity
dsvMIBObjects = _DsvMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1)
)
_DsvGlobal_ObjectIdentity = ObjectIdentity
dsvGlobal = _DsvGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 1)
)


class _DsvVlanId_Type(VlanIdOrNone):
    """Custom type dsvVlanId based on VlanIdOrNone"""
    defaultValue = 0


_DsvVlanId_Type.__name__ = "VlanIdOrNone"
_DsvVlanId_Object = MibScalar
dsvVlanId = _DsvVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 1, 1),
    _DsvVlanId_Type()
)
dsvVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsvVlanId.setStatus("current")


class _DsvQos_Type(Unsigned32):
    """Custom type dsvQos based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DsvQos_Type.__name__ = "Unsigned32"
_DsvQos_Object = MibScalar
dsvQos = _DsvQos_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 1, 2),
    _DsvQos_Type()
)
dsvQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsvQos.setStatus("current")


class _DsvAgingTime_Type(Unsigned32):
    """Custom type dsvAgingTime based on Unsigned32"""
    defaultValue = 720

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DsvAgingTime_Type.__name__ = "Unsigned32"
_DsvAgingTime_Object = MibScalar
dsvAgingTime = _DsvAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 1, 3),
    _DsvAgingTime_Type()
)
dsvAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsvAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    dsvAgingTime.setUnits("minutes")
_DsvOuiTable_Object = MibTable
dsvOuiTable = _DsvOuiTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 1, 4)
)
if mibBuilder.loadTexts:
    dsvOuiTable.setStatus("current")
_DsvOuiEntry_Object = MibTableRow
dsvOuiEntry = _DsvOuiEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 1, 4, 1)
)
dsvOuiEntry.setIndexNames(
    (0, "DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvOuiAddr"),
    (0, "DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvOuiMask"),
)
if mibBuilder.loadTexts:
    dsvOuiEntry.setStatus("current")
_DsvOuiAddr_Type = MacAddress
_DsvOuiAddr_Object = MibTableColumn
dsvOuiAddr = _DsvOuiAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 1, 4, 1, 1),
    _DsvOuiAddr_Type()
)
dsvOuiAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsvOuiAddr.setStatus("current")
_DsvOuiMask_Type = MacAddress
_DsvOuiMask_Object = MibTableColumn
dsvOuiMask = _DsvOuiMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 1, 4, 1, 2),
    _DsvOuiMask_Type()
)
dsvOuiMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsvOuiMask.setStatus("current")
_DsvOuiComponentType_Type = OuiComponentType
_DsvOuiComponentType_Object = MibTableColumn
dsvOuiComponentType = _DsvOuiComponentType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 1, 4, 1, 3),
    _DsvOuiComponentType_Type()
)
dsvOuiComponentType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsvOuiComponentType.setStatus("current")


class _DsvOuiDescription_Type(SnmpAdminString):
    """Custom type dsvOuiDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DsvOuiDescription_Type.__name__ = "SnmpAdminString"
_DsvOuiDescription_Object = MibTableColumn
dsvOuiDescription = _DsvOuiDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 1, 4, 1, 4),
    _DsvOuiDescription_Type()
)
dsvOuiDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsvOuiDescription.setStatus("current")
_DsvOuiRowStatus_Type = RowStatus
_DsvOuiRowStatus_Object = MibTableColumn
dsvOuiRowStatus = _DsvOuiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 1, 4, 1, 5),
    _DsvOuiRowStatus_Type()
)
dsvOuiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsvOuiRowStatus.setStatus("current")


class _DsvOnvifDiscoverPort_Type(Unsigned32):
    """Custom type dsvOnvifDiscoverPort based on Unsigned32"""
    defaultValue = 554


_DsvOnvifDiscoverPort_Type.__name__ = "Unsigned32"
_DsvOnvifDiscoverPort_Object = MibScalar
dsvOnvifDiscoverPort = _DsvOnvifDiscoverPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 1, 5),
    _DsvOnvifDiscoverPort_Type()
)
dsvOnvifDiscoverPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsvOnvifDiscoverPort.setStatus("current")
_DsvInterface_ObjectIdentity = ObjectIdentity
dsvInterface = _DsvInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 2)
)
_DsvInterfaceTable_Object = MibTable
dsvInterfaceTable = _DsvInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dsvInterfaceTable.setStatus("current")
_DsvInterfaceEntry_Object = MibTableRow
dsvInterfaceEntry = _DsvInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 2, 1, 1)
)
dsvInterfaceEntry.setIndexNames(
    (0, "DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvIfIndex"),
)
if mibBuilder.loadTexts:
    dsvInterfaceEntry.setStatus("current")
_DsvIfIndex_Type = InterfaceIndex
_DsvIfIndex_Object = MibTableColumn
dsvIfIndex = _DsvIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 2, 1, 1, 1),
    _DsvIfIndex_Type()
)
dsvIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsvIfIndex.setStatus("current")
_DsvIfEnabled_Type = TruthValue
_DsvIfEnabled_Object = MibTableColumn
dsvIfEnabled = _DsvIfEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 2, 1, 1, 2),
    _DsvIfEnabled_Type()
)
dsvIfEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsvIfEnabled.setStatus("current")
_DsvInfo_ObjectIdentity = ObjectIdentity
dsvInfo = _DsvInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 3)
)
_DsvMemberPorts_Type = PortList
_DsvMemberPorts_Object = MibScalar
dsvMemberPorts = _DsvMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 3, 1),
    _DsvMemberPorts_Type()
)
dsvMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsvMemberPorts.setStatus("current")
_DsvDynamicPorts_Type = PortList
_DsvDynamicPorts_Object = MibScalar
dsvDynamicPorts = _DsvDynamicPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 3, 2),
    _DsvDynamicPorts_Type()
)
dsvDynamicPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsvDynamicPorts.setStatus("current")
_DsvDeviceTable_Object = MibTable
dsvDeviceTable = _DsvDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 3, 3)
)
if mibBuilder.loadTexts:
    dsvDeviceTable.setStatus("current")
_DsvDeviceEntry_Object = MibTableRow
dsvDeviceEntry = _DsvDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 3, 3, 1)
)
dsvDeviceEntry.setIndexNames(
    (0, "DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvDevicePortIfIdx"),
    (0, "DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvDeviceAddr"),
)
if mibBuilder.loadTexts:
    dsvDeviceEntry.setStatus("current")
_DsvDevicePortIfIdx_Type = InterfaceIndex
_DsvDevicePortIfIdx_Object = MibTableColumn
dsvDevicePortIfIdx = _DsvDevicePortIfIdx_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 3, 3, 1, 1),
    _DsvDevicePortIfIdx_Type()
)
dsvDevicePortIfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsvDevicePortIfIdx.setStatus("current")
_DsvDeviceAddr_Type = MacAddress
_DsvDeviceAddr_Object = MibTableColumn
dsvDeviceAddr = _DsvDeviceAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 3, 3, 1, 2),
    _DsvDeviceAddr_Type()
)
dsvDeviceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsvDeviceAddr.setStatus("current")
_DsvDeviceCompType_Type = OuiComponentType
_DsvDeviceCompType_Object = MibTableColumn
dsvDeviceCompType = _DsvDeviceCompType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 3, 3, 1, 3),
    _DsvDeviceCompType_Type()
)
dsvDeviceCompType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsvDeviceCompType.setStatus("current")


class _DsvDeviceDescr_Type(SnmpAdminString):
    """Custom type dsvDeviceDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DsvDeviceDescr_Type.__name__ = "SnmpAdminString"
_DsvDeviceDescr_Object = MibTableColumn
dsvDeviceDescr = _DsvDeviceDescr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 3, 3, 1, 4),
    _DsvDeviceDescr_Type()
)
dsvDeviceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsvDeviceDescr.setStatus("current")
_DsvDeviceStartTime_Type = DateAndTime
_DsvDeviceStartTime_Object = MibTableColumn
dsvDeviceStartTime = _DsvDeviceStartTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 3, 3, 1, 5),
    _DsvDeviceStartTime_Type()
)
dsvDeviceStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsvDeviceStartTime.setStatus("current")


class _DsvDeviceStatus_Type(Integer32):
    """Custom type dsvDeviceStatus based on Integer32"""
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


_DsvDeviceStatus_Type.__name__ = "Integer32"
_DsvDeviceStatus_Object = MibTableColumn
dsvDeviceStatus = _DsvDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 3, 3, 1, 6),
    _DsvDeviceStatus_Type()
)
dsvDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsvDeviceStatus.setStatus("current")
_DsvOnvifIpcInfo_ObjectIdentity = ObjectIdentity
dsvOnvifIpcInfo = _DsvOnvifIpcInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 4)
)
_DsvOnvifIpcTable_Object = MibTable
dsvOnvifIpcTable = _DsvOnvifIpcTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dsvOnvifIpcTable.setStatus("current")
_DsvOnvifIpcEntry_Object = MibTableRow
dsvOnvifIpcEntry = _DsvOnvifIpcEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 4, 1, 1)
)
dsvOnvifIpcEntry.setIndexNames(
    (0, "DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvOnvifIpcIfIndex"),
    (0, "DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvOnvifIpcAddress"),
)
if mibBuilder.loadTexts:
    dsvOnvifIpcEntry.setStatus("current")
_DsvOnvifIpcIfIndex_Type = InterfaceIndex
_DsvOnvifIpcIfIndex_Object = MibTableColumn
dsvOnvifIpcIfIndex = _DsvOnvifIpcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 4, 1, 1, 1),
    _DsvOnvifIpcIfIndex_Type()
)
dsvOnvifIpcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsvOnvifIpcIfIndex.setStatus("current")
_DsvOnvifIpcAddress_Type = MacAddress
_DsvOnvifIpcAddress_Object = MibTableColumn
dsvOnvifIpcAddress = _DsvOnvifIpcAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 4, 1, 1, 2),
    _DsvOnvifIpcAddress_Type()
)
dsvOnvifIpcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsvOnvifIpcAddress.setStatus("current")
_DsvOnvifIpcIpAddress_Type = InetAddress
_DsvOnvifIpcIpAddress_Object = MibTableColumn
dsvOnvifIpcIpAddress = _DsvOnvifIpcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 4, 1, 1, 3),
    _DsvOnvifIpcIpAddress_Type()
)
dsvOnvifIpcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsvOnvifIpcIpAddress.setStatus("current")
_DsvOnvifIpcState_Type = TruthValue
_DsvOnvifIpcState_Object = MibTableColumn
dsvOnvifIpcState = _DsvOnvifIpcState_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 4, 1, 1, 4),
    _DsvOnvifIpcState_Type()
)
dsvOnvifIpcState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsvOnvifIpcState.setStatus("current")


class _DsvOnvifIpcModel_Type(SnmpAdminString):
    """Custom type dsvOnvifIpcModel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DsvOnvifIpcModel_Type.__name__ = "SnmpAdminString"
_DsvOnvifIpcModel_Object = MibTableColumn
dsvOnvifIpcModel = _DsvOnvifIpcModel_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 4, 1, 1, 5),
    _DsvOnvifIpcModel_Type()
)
dsvOnvifIpcModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsvOnvifIpcModel.setStatus("current")


class _DsvOnvifIpcManufacturer_Type(SnmpAdminString):
    """Custom type dsvOnvifIpcManufacturer based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DsvOnvifIpcManufacturer_Type.__name__ = "SnmpAdminString"
_DsvOnvifIpcManufacturer_Object = MibTableColumn
dsvOnvifIpcManufacturer = _DsvOnvifIpcManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 4, 1, 1, 6),
    _DsvOnvifIpcManufacturer_Type()
)
dsvOnvifIpcManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsvOnvifIpcManufacturer.setStatus("current")


class _DsvOnvifIpcDescription_Type(SnmpAdminString):
    """Custom type dsvOnvifIpcDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DsvOnvifIpcDescription_Type.__name__ = "SnmpAdminString"
_DsvOnvifIpcDescription_Object = MibTableColumn
dsvOnvifIpcDescription = _DsvOnvifIpcDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 4, 1, 1, 7),
    _DsvOnvifIpcDescription_Type()
)
dsvOnvifIpcDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsvOnvifIpcDescription.setStatus("current")
_DsvOnvifIpcThroughput_Type = Counter64
_DsvOnvifIpcThroughput_Object = MibTableColumn
dsvOnvifIpcThroughput = _DsvOnvifIpcThroughput_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 4, 1, 1, 8),
    _DsvOnvifIpcThroughput_Type()
)
dsvOnvifIpcThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsvOnvifIpcThroughput.setStatus("current")
if mibBuilder.loadTexts:
    dsvOnvifIpcThroughput.setUnits("Mbps")
_DsvOnvifNvrInfo_ObjectIdentity = ObjectIdentity
dsvOnvifNvrInfo = _DsvOnvifNvrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 5)
)
_DsvOnvifNvrTable_Object = MibTable
dsvOnvifNvrTable = _DsvOnvifNvrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 5, 1)
)
if mibBuilder.loadTexts:
    dsvOnvifNvrTable.setStatus("current")
_DsvOnvifNvrEntry_Object = MibTableRow
dsvOnvifNvrEntry = _DsvOnvifNvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 5, 1, 1)
)
dsvOnvifNvrEntry.setIndexNames(
    (0, "DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvOnvifNvrIfIndex"),
    (0, "DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvOnvifNvrAddress"),
)
if mibBuilder.loadTexts:
    dsvOnvifNvrEntry.setStatus("current")
_DsvOnvifNvrIfIndex_Type = InterfaceIndex
_DsvOnvifNvrIfIndex_Object = MibTableColumn
dsvOnvifNvrIfIndex = _DsvOnvifNvrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 5, 1, 1, 1),
    _DsvOnvifNvrIfIndex_Type()
)
dsvOnvifNvrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsvOnvifNvrIfIndex.setStatus("current")
_DsvOnvifNvrAddress_Type = MacAddress
_DsvOnvifNvrAddress_Object = MibTableColumn
dsvOnvifNvrAddress = _DsvOnvifNvrAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 5, 1, 1, 2),
    _DsvOnvifNvrAddress_Type()
)
dsvOnvifNvrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsvOnvifNvrAddress.setStatus("current")
_DsvOnvifNvrIpAddress_Type = InetAddress
_DsvOnvifNvrIpAddress_Object = MibTableColumn
dsvOnvifNvrIpAddress = _DsvOnvifNvrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 5, 1, 1, 3),
    _DsvOnvifNvrIpAddress_Type()
)
dsvOnvifNvrIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsvOnvifNvrIpAddress.setStatus("current")
_DsvOnvifNvrIpcNumber_Type = Unsigned32
_DsvOnvifNvrIpcNumber_Object = MibTableColumn
dsvOnvifNvrIpcNumber = _DsvOnvifNvrIpcNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 5, 1, 1, 4),
    _DsvOnvifNvrIpcNumber_Type()
)
dsvOnvifNvrIpcNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsvOnvifNvrIpcNumber.setStatus("current")
_DsvOnvifNvrThroughput_Type = Counter64
_DsvOnvifNvrThroughput_Object = MibTableColumn
dsvOnvifNvrThroughput = _DsvOnvifNvrThroughput_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 5, 1, 1, 5),
    _DsvOnvifNvrThroughput_Type()
)
dsvOnvifNvrThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsvOnvifNvrThroughput.setStatus("current")
if mibBuilder.loadTexts:
    dsvOnvifNvrThroughput.setUnits("Mbps")
_DsvOnvifNvrGroup_Type = Unsigned32
_DsvOnvifNvrGroup_Object = MibTableColumn
dsvOnvifNvrGroup = _DsvOnvifNvrGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 5, 1, 1, 6),
    _DsvOnvifNvrGroup_Type()
)
dsvOnvifNvrGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsvOnvifNvrGroup.setStatus("current")


class _DsvOnvifNvrDescription_Type(SnmpAdminString):
    """Custom type dsvOnvifNvrDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DsvOnvifNvrDescription_Type.__name__ = "SnmpAdminString"
_DsvOnvifNvrDescription_Object = MibTableColumn
dsvOnvifNvrDescription = _DsvOnvifNvrDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 5, 1, 1, 7),
    _DsvOnvifNvrDescription_Type()
)
dsvOnvifNvrDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsvOnvifNvrDescription.setStatus("current")
_DsvOnvifNvrGroupInfo_ObjectIdentity = ObjectIdentity
dsvOnvifNvrGroupInfo = _DsvOnvifNvrGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 6)
)
_DsvOnvifNvrGroupTable_Object = MibTable
dsvOnvifNvrGroupTable = _DsvOnvifNvrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 6, 1)
)
if mibBuilder.loadTexts:
    dsvOnvifNvrGroupTable.setStatus("current")
_DsvOnvifNvrGroupEntry_Object = MibTableRow
dsvOnvifNvrGroupEntry = _DsvOnvifNvrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 6, 1, 1)
)
dsvOnvifNvrGroupEntry.setIndexNames(
    (0, "DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvOnvifNvrGroupIfIndex"),
    (0, "DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvOnvifNvrGroupNvrAddress"),
    (0, "DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvOnvifNvrGroupIpcAddress"),
)
if mibBuilder.loadTexts:
    dsvOnvifNvrGroupEntry.setStatus("current")
_DsvOnvifNvrGroupIfIndex_Type = InterfaceIndex
_DsvOnvifNvrGroupIfIndex_Object = MibTableColumn
dsvOnvifNvrGroupIfIndex = _DsvOnvifNvrGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 6, 1, 1, 1),
    _DsvOnvifNvrGroupIfIndex_Type()
)
dsvOnvifNvrGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsvOnvifNvrGroupIfIndex.setStatus("current")
_DsvOnvifNvrGroupNvrAddress_Type = MacAddress
_DsvOnvifNvrGroupNvrAddress_Object = MibTableColumn
dsvOnvifNvrGroupNvrAddress = _DsvOnvifNvrGroupNvrAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 6, 1, 1, 2),
    _DsvOnvifNvrGroupNvrAddress_Type()
)
dsvOnvifNvrGroupNvrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsvOnvifNvrGroupNvrAddress.setStatus("current")
_DsvOnvifNvrGroupIpcAddress_Type = MacAddress
_DsvOnvifNvrGroupIpcAddress_Object = MibTableColumn
dsvOnvifNvrGroupIpcAddress = _DsvOnvifNvrGroupIpcAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 6, 1, 1, 3),
    _DsvOnvifNvrGroupIpcAddress_Type()
)
dsvOnvifNvrGroupIpcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsvOnvifNvrGroupIpcAddress.setStatus("current")
_DsvOnvifNvrGroupNvrIpAddress_Type = InetAddress
_DsvOnvifNvrGroupNvrIpAddress_Object = MibTableColumn
dsvOnvifNvrGroupNvrIpAddress = _DsvOnvifNvrGroupNvrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 6, 1, 1, 4),
    _DsvOnvifNvrGroupNvrIpAddress_Type()
)
dsvOnvifNvrGroupNvrIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsvOnvifNvrGroupNvrIpAddress.setStatus("current")
_DsvOnvifNvrGroupIpcIpAddress_Type = InetAddress
_DsvOnvifNvrGroupIpcIpAddress_Object = MibTableColumn
dsvOnvifNvrGroupIpcIpAddress = _DsvOnvifNvrGroupIpcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 6, 1, 1, 5),
    _DsvOnvifNvrGroupIpcIpAddress_Type()
)
dsvOnvifNvrGroupIpcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsvOnvifNvrGroupIpcIpAddress.setStatus("current")
_DsvOnvifNvrGroupNvrGroup_Type = Unsigned32
_DsvOnvifNvrGroupNvrGroup_Object = MibTableColumn
dsvOnvifNvrGroupNvrGroup = _DsvOnvifNvrGroupNvrGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 1, 6, 1, 1, 6),
    _DsvOnvifNvrGroupNvrGroup_Type()
)
dsvOnvifNvrGroupNvrGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsvOnvifNvrGroupNvrGroup.setStatus("current")
_DsvMIBConformance_ObjectIdentity = ObjectIdentity
dsvMIBConformance = _DsvMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 2)
)
_DsvMIBCompliances_ObjectIdentity = ObjectIdentity
dsvMIBCompliances = _DsvMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 2, 1)
)
_DsvMIBGroups_ObjectIdentity = ObjectIdentity
dsvMIBGroups = _DsvMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 2, 2)
)

# Managed Objects groups

dsvBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 2, 2, 1)
)
dsvBasicGroup.setObjects(
      *(("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvVlanId"),
        ("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvQos"),
        ("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvAgingTime"),
        ("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvOnvifDiscoverPort"),
        ("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvIfEnabled"),
        ("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvMemberPorts"),
        ("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvDynamicPorts"))
)
if mibBuilder.loadTexts:
    dsvBasicGroup.setStatus("current")

dsvOUICfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 2, 2, 2)
)
dsvOUICfgGroup.setObjects(
      *(("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvOuiComponentType"),
        ("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvOuiDescription"),
        ("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvOuiRowStatus"))
)
if mibBuilder.loadTexts:
    dsvOUICfgGroup.setStatus("current")

dsvDeviceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 2, 2, 3)
)
dsvDeviceInfoGroup.setObjects(
      *(("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvDeviceCompType"),
        ("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvDeviceDescr"),
        ("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvDeviceStartTime"),
        ("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvDeviceStatus"))
)
if mibBuilder.loadTexts:
    dsvDeviceInfoGroup.setStatus("current")

dsvOnvifIpcCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 2, 2, 4)
)
dsvOnvifIpcCfgGroup.setObjects(
      *(("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvOnvifIpcIpAddress"),
        ("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvOnvifIpcState"),
        ("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvOnvifIpcModel"),
        ("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvOnvifIpcManufacturer"),
        ("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvOnvifIpcDescription"),
        ("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvOnvifIpcThroughput"))
)
if mibBuilder.loadTexts:
    dsvOnvifIpcCfgGroup.setStatus("current")

dsvOnvifNvrCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 2, 2, 5)
)
dsvOnvifNvrCfgGroup.setObjects(
      *(("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvOnvifNvrIpAddress"),
        ("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvOnvifNvrIpcNumber"),
        ("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvOnvifNvrThroughput"),
        ("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvOnvifNvrGroup"),
        ("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvOnvifNvrDescription"))
)
if mibBuilder.loadTexts:
    dsvOnvifNvrCfgGroup.setStatus("current")

dsvOnvifNvrGroupCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 2, 2, 6)
)
dsvOnvifNvrGroupCfgGroup.setObjects(
      *(("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvOnvifNvrGroupNvrIpAddress"),
        ("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvOnvifNvrGroupIpcIpAddress"),
        ("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvOnvifNvrGroupNvrGroup"))
)
if mibBuilder.loadTexts:
    dsvOnvifNvrGroupCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dsvMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 34, 2, 1, 1)
)
dsvMIBCompliance.setObjects(
      *(("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvBasicGroup"),
        ("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvOUICfgGroup"),
        ("DLINKSW-SURVEILLANCE-VLAN-MIB", "dsvDeviceInfoGroup"))
)
if mibBuilder.loadTexts:
    dsvMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-SURVEILLANCE-VLAN-MIB",
    **{"OuiComponentType": OuiComponentType,
       "dlinkSwSurveillanceVlanMIB": dlinkSwSurveillanceVlanMIB,
       "dsvMIBNotifications": dsvMIBNotifications,
       "dsvMIBObjects": dsvMIBObjects,
       "dsvGlobal": dsvGlobal,
       "dsvVlanId": dsvVlanId,
       "dsvQos": dsvQos,
       "dsvAgingTime": dsvAgingTime,
       "dsvOuiTable": dsvOuiTable,
       "dsvOuiEntry": dsvOuiEntry,
       "dsvOuiAddr": dsvOuiAddr,
       "dsvOuiMask": dsvOuiMask,
       "dsvOuiComponentType": dsvOuiComponentType,
       "dsvOuiDescription": dsvOuiDescription,
       "dsvOuiRowStatus": dsvOuiRowStatus,
       "dsvOnvifDiscoverPort": dsvOnvifDiscoverPort,
       "dsvInterface": dsvInterface,
       "dsvInterfaceTable": dsvInterfaceTable,
       "dsvInterfaceEntry": dsvInterfaceEntry,
       "dsvIfIndex": dsvIfIndex,
       "dsvIfEnabled": dsvIfEnabled,
       "dsvInfo": dsvInfo,
       "dsvMemberPorts": dsvMemberPorts,
       "dsvDynamicPorts": dsvDynamicPorts,
       "dsvDeviceTable": dsvDeviceTable,
       "dsvDeviceEntry": dsvDeviceEntry,
       "dsvDevicePortIfIdx": dsvDevicePortIfIdx,
       "dsvDeviceAddr": dsvDeviceAddr,
       "dsvDeviceCompType": dsvDeviceCompType,
       "dsvDeviceDescr": dsvDeviceDescr,
       "dsvDeviceStartTime": dsvDeviceStartTime,
       "dsvDeviceStatus": dsvDeviceStatus,
       "dsvOnvifIpcInfo": dsvOnvifIpcInfo,
       "dsvOnvifIpcTable": dsvOnvifIpcTable,
       "dsvOnvifIpcEntry": dsvOnvifIpcEntry,
       "dsvOnvifIpcIfIndex": dsvOnvifIpcIfIndex,
       "dsvOnvifIpcAddress": dsvOnvifIpcAddress,
       "dsvOnvifIpcIpAddress": dsvOnvifIpcIpAddress,
       "dsvOnvifIpcState": dsvOnvifIpcState,
       "dsvOnvifIpcModel": dsvOnvifIpcModel,
       "dsvOnvifIpcManufacturer": dsvOnvifIpcManufacturer,
       "dsvOnvifIpcDescription": dsvOnvifIpcDescription,
       "dsvOnvifIpcThroughput": dsvOnvifIpcThroughput,
       "dsvOnvifNvrInfo": dsvOnvifNvrInfo,
       "dsvOnvifNvrTable": dsvOnvifNvrTable,
       "dsvOnvifNvrEntry": dsvOnvifNvrEntry,
       "dsvOnvifNvrIfIndex": dsvOnvifNvrIfIndex,
       "dsvOnvifNvrAddress": dsvOnvifNvrAddress,
       "dsvOnvifNvrIpAddress": dsvOnvifNvrIpAddress,
       "dsvOnvifNvrIpcNumber": dsvOnvifNvrIpcNumber,
       "dsvOnvifNvrThroughput": dsvOnvifNvrThroughput,
       "dsvOnvifNvrGroup": dsvOnvifNvrGroup,
       "dsvOnvifNvrDescription": dsvOnvifNvrDescription,
       "dsvOnvifNvrGroupInfo": dsvOnvifNvrGroupInfo,
       "dsvOnvifNvrGroupTable": dsvOnvifNvrGroupTable,
       "dsvOnvifNvrGroupEntry": dsvOnvifNvrGroupEntry,
       "dsvOnvifNvrGroupIfIndex": dsvOnvifNvrGroupIfIndex,
       "dsvOnvifNvrGroupNvrAddress": dsvOnvifNvrGroupNvrAddress,
       "dsvOnvifNvrGroupIpcAddress": dsvOnvifNvrGroupIpcAddress,
       "dsvOnvifNvrGroupNvrIpAddress": dsvOnvifNvrGroupNvrIpAddress,
       "dsvOnvifNvrGroupIpcIpAddress": dsvOnvifNvrGroupIpcIpAddress,
       "dsvOnvifNvrGroupNvrGroup": dsvOnvifNvrGroupNvrGroup,
       "dsvMIBConformance": dsvMIBConformance,
       "dsvMIBCompliances": dsvMIBCompliances,
       "dsvMIBCompliance": dsvMIBCompliance,
       "dsvMIBGroups": dsvMIBGroups,
       "dsvBasicGroup": dsvBasicGroup,
       "dsvOUICfgGroup": dsvOUICfgGroup,
       "dsvDeviceInfoGroup": dsvDeviceInfoGroup,
       "dsvOnvifIpcCfgGroup": dsvOnvifIpcCfgGroup,
       "dsvOnvifNvrCfgGroup": dsvOnvifNvrCfgGroup,
       "dsvOnvifNvrGroupCfgGroup": dsvOnvifNvrGroupCfgGroup}
)
