# SNMP MIB module (TN-MVR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-MVR-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:32:04 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(PortList,
 VlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnMVRMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnMVRMIBNotifications_ObjectIdentity = ObjectIdentity
tnMVRMIBNotifications = _TnMVRMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 1)
)
_TnMVRMIBObjects_ObjectIdentity = ObjectIdentity
tnMVRMIBObjects = _TnMVRMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2)
)
_TnMVRMIBMgmt_ObjectIdentity = ObjectIdentity
tnMVRMIBMgmt = _TnMVRMIBMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1)
)
_TnMVRModeTable_Object = MibTable
tnMVRModeTable = _TnMVRModeTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnMVRModeTable.setStatus("current")
_TnMVRModeEntry_Object = MibTableRow
tnMVRModeEntry = _TnMVRModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 1, 1)
)
tnMVRModeEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnMVRModeEntry.setStatus("current")
_TnMVRMode_Type = TruthValue
_TnMVRMode_Object = MibTableColumn
tnMVRMode = _TnMVRMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 1, 1, 1),
    _TnMVRMode_Type()
)
tnMVRMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMVRMode.setStatus("current")
_TnMVRStatisticsClear_Type = TruthValue
_TnMVRStatisticsClear_Object = MibTableColumn
tnMVRStatisticsClear = _TnMVRStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 1, 1, 2),
    _TnMVRStatisticsClear_Type()
)
tnMVRStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMVRStatisticsClear.setStatus("current")
_TnMVRInterfaceTable_Object = MibTable
tnMVRInterfaceTable = _TnMVRInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tnMVRInterfaceTable.setStatus("current")
_TnMVRInterfaceEntry_Object = MibTableRow
tnMVRInterfaceEntry = _TnMVRInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 2, 1)
)
tnMVRInterfaceEntry.setIndexNames(
    (0, "TN-MVR-MIB", "tnMVRVID"),
)
if mibBuilder.loadTexts:
    tnMVRInterfaceEntry.setStatus("current")
_TnMVRVID_Type = VlanIndex
_TnMVRVID_Object = MibTableColumn
tnMVRVID = _TnMVRVID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 2, 1, 1),
    _TnMVRVID_Type()
)
tnMVRVID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMVRVID.setStatus("current")


class _TnMVRName_Type(DisplayString):
    """Custom type tnMVRName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnMVRName_Type.__name__ = "DisplayString"
_TnMVRName_Object = MibTableColumn
tnMVRName = _TnMVRName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 2, 1, 2),
    _TnMVRName_Type()
)
tnMVRName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMVRName.setStatus("current")


class _TnMVRInterfaceMode_Type(Integer32):
    """Custom type tnMVRInterfaceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("compatible", 2))
    )


_TnMVRInterfaceMode_Type.__name__ = "Integer32"
_TnMVRInterfaceMode_Object = MibTableColumn
tnMVRInterfaceMode = _TnMVRInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 2, 1, 3),
    _TnMVRInterfaceMode_Type()
)
tnMVRInterfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMVRInterfaceMode.setStatus("current")


class _TnMVRInterfaceTagging_Type(Integer32):
    """Custom type tnMVRInterfaceTagging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("untagged", 1),
          ("tagged", 2))
    )


_TnMVRInterfaceTagging_Type.__name__ = "Integer32"
_TnMVRInterfaceTagging_Object = MibTableColumn
tnMVRInterfaceTagging = _TnMVRInterfaceTagging_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 2, 1, 4),
    _TnMVRInterfaceTagging_Type()
)
tnMVRInterfaceTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMVRInterfaceTagging.setStatus("current")


class _TnMVRInterfacePriority_Type(Integer32):
    """Custom type tnMVRInterfacePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMVRInterfacePriority_Type.__name__ = "Integer32"
_TnMVRInterfacePriority_Object = MibTableColumn
tnMVRInterfacePriority = _TnMVRInterfacePriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 2, 1, 5),
    _TnMVRInterfacePriority_Type()
)
tnMVRInterfacePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMVRInterfacePriority.setStatus("current")


class _TnMVRInterfaceLLQI_Type(Integer32):
    """Custom type tnMVRInterfaceLLQI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31744),
    )


_TnMVRInterfaceLLQI_Type.__name__ = "Integer32"
_TnMVRInterfaceLLQI_Object = MibTableColumn
tnMVRInterfaceLLQI = _TnMVRInterfaceLLQI_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 2, 1, 6),
    _TnMVRInterfaceLLQI_Type()
)
tnMVRInterfaceLLQI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMVRInterfaceLLQI.setStatus("current")
_TnMVRInactivePortList_Type = PortList
_TnMVRInactivePortList_Object = MibTableColumn
tnMVRInactivePortList = _TnMVRInactivePortList_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 2, 1, 7),
    _TnMVRInactivePortList_Type()
)
tnMVRInactivePortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMVRInactivePortList.setStatus("current")
_TnMVRSourcePortList_Type = PortList
_TnMVRSourcePortList_Object = MibTableColumn
tnMVRSourcePortList = _TnMVRSourcePortList_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 2, 1, 8),
    _TnMVRSourcePortList_Type()
)
tnMVRSourcePortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMVRSourcePortList.setStatus("current")
_TnMVRReceiverPortList_Type = PortList
_TnMVRReceiverPortList_Object = MibTableColumn
tnMVRReceiverPortList = _TnMVRReceiverPortList_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 2, 1, 9),
    _TnMVRReceiverPortList_Type()
)
tnMVRReceiverPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMVRReceiverPortList.setStatus("current")
_TnMVRInterfaceRowStatus_Type = RowStatus
_TnMVRInterfaceRowStatus_Object = MibTableColumn
tnMVRInterfaceRowStatus = _TnMVRInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 2, 1, 10),
    _TnMVRInterfaceRowStatus_Type()
)
tnMVRInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMVRInterfaceRowStatus.setStatus("current")
_TnMVRImmediateLeaveTable_Object = MibTable
tnMVRImmediateLeaveTable = _TnMVRImmediateLeaveTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tnMVRImmediateLeaveTable.setStatus("current")
_TnMVRImmediateLeaveEntry_Object = MibTableRow
tnMVRImmediateLeaveEntry = _TnMVRImmediateLeaveEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 3, 1)
)
tnMVRImmediateLeaveEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnMVRImmediateLeaveEntry.setStatus("current")
_TnMVRImmediateLeaveEnabled_Type = TruthValue
_TnMVRImmediateLeaveEnabled_Object = MibTableColumn
tnMVRImmediateLeaveEnabled = _TnMVRImmediateLeaveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 3, 1, 1),
    _TnMVRImmediateLeaveEnabled_Type()
)
tnMVRImmediateLeaveEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMVRImmediateLeaveEnabled.setStatus("current")
_TnMVRChannelConfigTable_Object = MibTable
tnMVRChannelConfigTable = _TnMVRChannelConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tnMVRChannelConfigTable.setStatus("current")
_TnMVRChannelConfigEntry_Object = MibTableRow
tnMVRChannelConfigEntry = _TnMVRChannelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 4, 1)
)
tnMVRChannelConfigEntry.setIndexNames(
    (0, "TN-MVR-MIB", "tnMVRChannelVID"),
    (0, "TN-MVR-MIB", "tnMVRChannelStartEndAddrType"),
    (0, "TN-MVR-MIB", "tnMVRChannelStartAddr"),
)
if mibBuilder.loadTexts:
    tnMVRChannelConfigEntry.setStatus("current")
_TnMVRChannelVID_Type = VlanIndex
_TnMVRChannelVID_Object = MibTableColumn
tnMVRChannelVID = _TnMVRChannelVID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 4, 1, 1),
    _TnMVRChannelVID_Type()
)
tnMVRChannelVID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMVRChannelVID.setStatus("current")
_TnMVRChannelStartEndAddrType_Type = InetAddressType
_TnMVRChannelStartEndAddrType_Object = MibTableColumn
tnMVRChannelStartEndAddrType = _TnMVRChannelStartEndAddrType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 4, 1, 2),
    _TnMVRChannelStartEndAddrType_Type()
)
tnMVRChannelStartEndAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMVRChannelStartEndAddrType.setStatus("current")
_TnMVRChannelStartAddr_Type = InetAddress
_TnMVRChannelStartAddr_Object = MibTableColumn
tnMVRChannelStartAddr = _TnMVRChannelStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 4, 1, 3),
    _TnMVRChannelStartAddr_Type()
)
tnMVRChannelStartAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMVRChannelStartAddr.setStatus("current")
_TnMVRChannelEndAddr_Type = InetAddress
_TnMVRChannelEndAddr_Object = MibTableColumn
tnMVRChannelEndAddr = _TnMVRChannelEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 4, 1, 4),
    _TnMVRChannelEndAddr_Type()
)
tnMVRChannelEndAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMVRChannelEndAddr.setStatus("current")


class _TnMVRChannelName_Type(DisplayString):
    """Custom type tnMVRChannelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnMVRChannelName_Type.__name__ = "DisplayString"
_TnMVRChannelName_Object = MibTableColumn
tnMVRChannelName = _TnMVRChannelName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 4, 1, 5),
    _TnMVRChannelName_Type()
)
tnMVRChannelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMVRChannelName.setStatus("current")
_TnMVRChannelRowStatus_Type = RowStatus
_TnMVRChannelRowStatus_Object = MibTableColumn
tnMVRChannelRowStatus = _TnMVRChannelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 4, 1, 6),
    _TnMVRChannelRowStatus_Type()
)
tnMVRChannelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMVRChannelRowStatus.setStatus("current")
_TnMVRStatisticsTable_Object = MibTable
tnMVRStatisticsTable = _TnMVRStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 5)
)
if mibBuilder.loadTexts:
    tnMVRStatisticsTable.setStatus("current")
_TnMVRStatisticsEntry_Object = MibTableRow
tnMVRStatisticsEntry = _TnMVRStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 5, 1)
)
tnMVRStatisticsEntry.setIndexNames(
    (0, "TN-MVR-MIB", "tnMVRStatisticsVID"),
)
if mibBuilder.loadTexts:
    tnMVRStatisticsEntry.setStatus("current")


class _TnMVRStatisticsVID_Type(Integer32):
    """Custom type tnMVRStatisticsVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_TnMVRStatisticsVID_Type.__name__ = "Integer32"
_TnMVRStatisticsVID_Object = MibTableColumn
tnMVRStatisticsVID = _TnMVRStatisticsVID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 5, 1, 1),
    _TnMVRStatisticsVID_Type()
)
tnMVRStatisticsVID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMVRStatisticsVID.setStatus("current")
_TnMVRIGMPQueriesRx_Type = Unsigned32
_TnMVRIGMPQueriesRx_Object = MibTableColumn
tnMVRIGMPQueriesRx = _TnMVRIGMPQueriesRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 5, 1, 2),
    _TnMVRIGMPQueriesRx_Type()
)
tnMVRIGMPQueriesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMVRIGMPQueriesRx.setStatus("current")
_TnMVRMLDQueriesRx_Type = Unsigned32
_TnMVRMLDQueriesRx_Object = MibTableColumn
tnMVRMLDQueriesRx = _TnMVRMLDQueriesRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 5, 1, 3),
    _TnMVRMLDQueriesRx_Type()
)
tnMVRMLDQueriesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMVRMLDQueriesRx.setStatus("current")
_TnMVRIGMPQueriesTx_Type = Unsigned32
_TnMVRIGMPQueriesTx_Object = MibTableColumn
tnMVRIGMPQueriesTx = _TnMVRIGMPQueriesTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 5, 1, 4),
    _TnMVRIGMPQueriesTx_Type()
)
tnMVRIGMPQueriesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMVRIGMPQueriesTx.setStatus("current")
_TnMVRMLDQueriesTx_Type = Unsigned32
_TnMVRMLDQueriesTx_Object = MibTableColumn
tnMVRMLDQueriesTx = _TnMVRMLDQueriesTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 5, 1, 5),
    _TnMVRMLDQueriesTx_Type()
)
tnMVRMLDQueriesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMVRMLDQueriesTx.setStatus("current")
_TnMVRIGMPv1JoinsRx_Type = Unsigned32
_TnMVRIGMPv1JoinsRx_Object = MibTableColumn
tnMVRIGMPv1JoinsRx = _TnMVRIGMPv1JoinsRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 5, 1, 6),
    _TnMVRIGMPv1JoinsRx_Type()
)
tnMVRIGMPv1JoinsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMVRIGMPv1JoinsRx.setStatus("current")
_TnMVRIGMPv2ReportsRx_Type = Unsigned32
_TnMVRIGMPv2ReportsRx_Object = MibTableColumn
tnMVRIGMPv2ReportsRx = _TnMVRIGMPv2ReportsRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 5, 1, 7),
    _TnMVRIGMPv2ReportsRx_Type()
)
tnMVRIGMPv2ReportsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMVRIGMPv2ReportsRx.setStatus("current")
_TnMVRMLDv1ReportsRx_Type = Unsigned32
_TnMVRMLDv1ReportsRx_Object = MibTableColumn
tnMVRMLDv1ReportsRx = _TnMVRMLDv1ReportsRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 5, 1, 8),
    _TnMVRMLDv1ReportsRx_Type()
)
tnMVRMLDv1ReportsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMVRMLDv1ReportsRx.setStatus("current")
_TnMVRIGMPv3ReportsRx_Type = Unsigned32
_TnMVRIGMPv3ReportsRx_Object = MibTableColumn
tnMVRIGMPv3ReportsRx = _TnMVRIGMPv3ReportsRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 5, 1, 9),
    _TnMVRIGMPv3ReportsRx_Type()
)
tnMVRIGMPv3ReportsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMVRIGMPv3ReportsRx.setStatus("current")
_TnMVRMLDv2ReportsRx_Type = Unsigned32
_TnMVRMLDv2ReportsRx_Object = MibTableColumn
tnMVRMLDv2ReportsRx = _TnMVRMLDv2ReportsRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 5, 1, 10),
    _TnMVRMLDv2ReportsRx_Type()
)
tnMVRMLDv2ReportsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMVRMLDv2ReportsRx.setStatus("current")
_TnMVRIGMPv2LeavesRx_Type = Unsigned32
_TnMVRIGMPv2LeavesRx_Object = MibTableColumn
tnMVRIGMPv2LeavesRx = _TnMVRIGMPv2LeavesRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 5, 1, 11),
    _TnMVRIGMPv2LeavesRx_Type()
)
tnMVRIGMPv2LeavesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMVRIGMPv2LeavesRx.setStatus("current")
_TnMVRMLDv1LeavesRx_Type = Unsigned32
_TnMVRMLDv1LeavesRx_Object = MibTableColumn
tnMVRMLDv1LeavesRx = _TnMVRMLDv1LeavesRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 5, 1, 12),
    _TnMVRMLDv1LeavesRx_Type()
)
tnMVRMLDv1LeavesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMVRMLDv1LeavesRx.setStatus("current")
_TnMVRGroupInfoTable_Object = MibTable
tnMVRGroupInfoTable = _TnMVRGroupInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 6)
)
if mibBuilder.loadTexts:
    tnMVRGroupInfoTable.setStatus("current")
_TnMVRGroupInfoEntry_Object = MibTableRow
tnMVRGroupInfoEntry = _TnMVRGroupInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 6, 1)
)
tnMVRGroupInfoEntry.setIndexNames(
    (0, "TN-MVR-MIB", "tnMVRGroupVID"),
    (0, "TN-MVR-MIB", "tnMVRGroupAddrType"),
    (0, "TN-MVR-MIB", "tnMVRGroupAddr"),
)
if mibBuilder.loadTexts:
    tnMVRGroupInfoEntry.setStatus("current")


class _TnMVRGroupVID_Type(Integer32):
    """Custom type tnMVRGroupVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_TnMVRGroupVID_Type.__name__ = "Integer32"
_TnMVRGroupVID_Object = MibTableColumn
tnMVRGroupVID = _TnMVRGroupVID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 6, 1, 1),
    _TnMVRGroupVID_Type()
)
tnMVRGroupVID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMVRGroupVID.setStatus("current")
_TnMVRGroupAddrType_Type = InetAddressType
_TnMVRGroupAddrType_Object = MibTableColumn
tnMVRGroupAddrType = _TnMVRGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 6, 1, 2),
    _TnMVRGroupAddrType_Type()
)
tnMVRGroupAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMVRGroupAddrType.setStatus("current")
_TnMVRGroupAddr_Type = InetAddress
_TnMVRGroupAddr_Object = MibTableColumn
tnMVRGroupAddr = _TnMVRGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 6, 1, 3),
    _TnMVRGroupAddr_Type()
)
tnMVRGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMVRGroupAddr.setStatus("current")
_TnMVRGroupPortMembers_Type = PortList
_TnMVRGroupPortMembers_Object = MibTableColumn
tnMVRGroupPortMembers = _TnMVRGroupPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 6, 1, 4),
    _TnMVRGroupPortMembers_Type()
)
tnMVRGroupPortMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMVRGroupPortMembers.setStatus("current")
_TnMVRSFMTable_Object = MibTable
tnMVRSFMTable = _TnMVRSFMTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 7)
)
if mibBuilder.loadTexts:
    tnMVRSFMTable.setStatus("current")
_TnMVRSFMEntry_Object = MibTableRow
tnMVRSFMEntry = _TnMVRSFMEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 7, 1)
)
tnMVRSFMEntry.setIndexNames(
    (0, "TN-MVR-MIB", "tnMVRSFMVID"),
    (0, "TN-MVR-MIB", "tnMVRSFMGroupAddrType"),
    (0, "TN-MVR-MIB", "tnMVRSFMGroupAddr"),
    (0, "TN-MVR-MIB", "tnMVRSFMIfIndex"),
    (0, "TN-MVR-MIB", "tnMVRSFMMode"),
    (0, "TN-MVR-MIB", "tnMVRSFMSourceAddrType"),
    (0, "TN-MVR-MIB", "tnMVRSFMSourceAddr"),
)
if mibBuilder.loadTexts:
    tnMVRSFMEntry.setStatus("current")


class _TnMVRSFMVID_Type(Integer32):
    """Custom type tnMVRSFMVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_TnMVRSFMVID_Type.__name__ = "Integer32"
_TnMVRSFMVID_Object = MibTableColumn
tnMVRSFMVID = _TnMVRSFMVID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 7, 1, 1),
    _TnMVRSFMVID_Type()
)
tnMVRSFMVID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMVRSFMVID.setStatus("current")
_TnMVRSFMGroupAddrType_Type = InetAddressType
_TnMVRSFMGroupAddrType_Object = MibTableColumn
tnMVRSFMGroupAddrType = _TnMVRSFMGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 7, 1, 2),
    _TnMVRSFMGroupAddrType_Type()
)
tnMVRSFMGroupAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMVRSFMGroupAddrType.setStatus("current")
_TnMVRSFMGroupAddr_Type = InetAddress
_TnMVRSFMGroupAddr_Object = MibTableColumn
tnMVRSFMGroupAddr = _TnMVRSFMGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 7, 1, 3),
    _TnMVRSFMGroupAddr_Type()
)
tnMVRSFMGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMVRSFMGroupAddr.setStatus("current")
_TnMVRSFMIfIndex_Type = InterfaceIndex
_TnMVRSFMIfIndex_Object = MibTableColumn
tnMVRSFMIfIndex = _TnMVRSFMIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 7, 1, 4),
    _TnMVRSFMIfIndex_Type()
)
tnMVRSFMIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMVRSFMIfIndex.setStatus("current")


class _TnMVRSFMMode_Type(Integer32):
    """Custom type tnMVRSFMMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("include", 1),
          ("exclude", 2))
    )


_TnMVRSFMMode_Type.__name__ = "Integer32"
_TnMVRSFMMode_Object = MibTableColumn
tnMVRSFMMode = _TnMVRSFMMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 7, 1, 5),
    _TnMVRSFMMode_Type()
)
tnMVRSFMMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMVRSFMMode.setStatus("current")
_TnMVRSFMSourceAddrType_Type = InetAddressType
_TnMVRSFMSourceAddrType_Object = MibTableColumn
tnMVRSFMSourceAddrType = _TnMVRSFMSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 7, 1, 6),
    _TnMVRSFMSourceAddrType_Type()
)
tnMVRSFMSourceAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMVRSFMSourceAddrType.setStatus("current")
_TnMVRSFMSourceAddr_Type = InetAddress
_TnMVRSFMSourceAddr_Object = MibTableColumn
tnMVRSFMSourceAddr = _TnMVRSFMSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 7, 1, 7),
    _TnMVRSFMSourceAddr_Type()
)
tnMVRSFMSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMVRSFMSourceAddr.setStatus("current")


class _TnMVRSFMType_Type(Integer32):
    """Custom type tnMVRSFMType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_TnMVRSFMType_Type.__name__ = "Integer32"
_TnMVRSFMType_Object = MibTableColumn
tnMVRSFMType = _TnMVRSFMType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 7, 1, 8),
    _TnMVRSFMType_Type()
)
tnMVRSFMType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMVRSFMType.setStatus("current")
_TnMVRSFMHardwareFilter_Type = TruthValue
_TnMVRSFMHardwareFilter_Object = MibTableColumn
tnMVRSFMHardwareFilter = _TnMVRSFMHardwareFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 2, 1, 7, 1, 9),
    _TnMVRSFMHardwareFilter_Type()
)
tnMVRSFMHardwareFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMVRSFMHardwareFilter.setStatus("current")
_TnMVRMIBConformance_ObjectIdentity = ObjectIdentity
tnMVRMIBConformance = _TnMVRMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 50, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-MVR-MIB",
    **{"tnMVRMIB": tnMVRMIB,
       "tnMVRMIBNotifications": tnMVRMIBNotifications,
       "tnMVRMIBObjects": tnMVRMIBObjects,
       "tnMVRMIBMgmt": tnMVRMIBMgmt,
       "tnMVRModeTable": tnMVRModeTable,
       "tnMVRModeEntry": tnMVRModeEntry,
       "tnMVRMode": tnMVRMode,
       "tnMVRStatisticsClear": tnMVRStatisticsClear,
       "tnMVRInterfaceTable": tnMVRInterfaceTable,
       "tnMVRInterfaceEntry": tnMVRInterfaceEntry,
       "tnMVRVID": tnMVRVID,
       "tnMVRName": tnMVRName,
       "tnMVRInterfaceMode": tnMVRInterfaceMode,
       "tnMVRInterfaceTagging": tnMVRInterfaceTagging,
       "tnMVRInterfacePriority": tnMVRInterfacePriority,
       "tnMVRInterfaceLLQI": tnMVRInterfaceLLQI,
       "tnMVRInactivePortList": tnMVRInactivePortList,
       "tnMVRSourcePortList": tnMVRSourcePortList,
       "tnMVRReceiverPortList": tnMVRReceiverPortList,
       "tnMVRInterfaceRowStatus": tnMVRInterfaceRowStatus,
       "tnMVRImmediateLeaveTable": tnMVRImmediateLeaveTable,
       "tnMVRImmediateLeaveEntry": tnMVRImmediateLeaveEntry,
       "tnMVRImmediateLeaveEnabled": tnMVRImmediateLeaveEnabled,
       "tnMVRChannelConfigTable": tnMVRChannelConfigTable,
       "tnMVRChannelConfigEntry": tnMVRChannelConfigEntry,
       "tnMVRChannelVID": tnMVRChannelVID,
       "tnMVRChannelStartEndAddrType": tnMVRChannelStartEndAddrType,
       "tnMVRChannelStartAddr": tnMVRChannelStartAddr,
       "tnMVRChannelEndAddr": tnMVRChannelEndAddr,
       "tnMVRChannelName": tnMVRChannelName,
       "tnMVRChannelRowStatus": tnMVRChannelRowStatus,
       "tnMVRStatisticsTable": tnMVRStatisticsTable,
       "tnMVRStatisticsEntry": tnMVRStatisticsEntry,
       "tnMVRStatisticsVID": tnMVRStatisticsVID,
       "tnMVRIGMPQueriesRx": tnMVRIGMPQueriesRx,
       "tnMVRMLDQueriesRx": tnMVRMLDQueriesRx,
       "tnMVRIGMPQueriesTx": tnMVRIGMPQueriesTx,
       "tnMVRMLDQueriesTx": tnMVRMLDQueriesTx,
       "tnMVRIGMPv1JoinsRx": tnMVRIGMPv1JoinsRx,
       "tnMVRIGMPv2ReportsRx": tnMVRIGMPv2ReportsRx,
       "tnMVRMLDv1ReportsRx": tnMVRMLDv1ReportsRx,
       "tnMVRIGMPv3ReportsRx": tnMVRIGMPv3ReportsRx,
       "tnMVRMLDv2ReportsRx": tnMVRMLDv2ReportsRx,
       "tnMVRIGMPv2LeavesRx": tnMVRIGMPv2LeavesRx,
       "tnMVRMLDv1LeavesRx": tnMVRMLDv1LeavesRx,
       "tnMVRGroupInfoTable": tnMVRGroupInfoTable,
       "tnMVRGroupInfoEntry": tnMVRGroupInfoEntry,
       "tnMVRGroupVID": tnMVRGroupVID,
       "tnMVRGroupAddrType": tnMVRGroupAddrType,
       "tnMVRGroupAddr": tnMVRGroupAddr,
       "tnMVRGroupPortMembers": tnMVRGroupPortMembers,
       "tnMVRSFMTable": tnMVRSFMTable,
       "tnMVRSFMEntry": tnMVRSFMEntry,
       "tnMVRSFMVID": tnMVRSFMVID,
       "tnMVRSFMGroupAddrType": tnMVRSFMGroupAddrType,
       "tnMVRSFMGroupAddr": tnMVRSFMGroupAddr,
       "tnMVRSFMIfIndex": tnMVRSFMIfIndex,
       "tnMVRSFMMode": tnMVRSFMMode,
       "tnMVRSFMSourceAddrType": tnMVRSFMSourceAddrType,
       "tnMVRSFMSourceAddr": tnMVRSFMSourceAddr,
       "tnMVRSFMType": tnMVRSFMType,
       "tnMVRSFMHardwareFilter": tnMVRSFMHardwareFilter,
       "tnMVRMIBConformance": tnMVRMIBConformance}
)
