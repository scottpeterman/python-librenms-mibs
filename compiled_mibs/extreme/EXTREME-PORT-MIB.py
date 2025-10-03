# SNMP MIB module (EXTREME-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\extreme\EXTREME-PORT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:43:36 2025
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

(ClientAuthType,
 extremeAgent) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "ClientAuthType",
    "extremeAgent")

(extremeVlanIfIndex,) = mibBuilder.importSymbols(
    "EXTREME-VLAN-MIB",
    "extremeVlanIfIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

extremePort = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4)
)
if mibBuilder.loadTexts:
    extremePort.setRevisions(
        ("2019-03-21 01:00",
         "2018-03-13 00:00")
    )


# Types definitions



class ExtremePortTrafficDirection(Integer32):
    """Custom type ExtremePortTrafficDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremePortLoadshareTable_Object = MibTable
extremePortLoadshareTable = _ExtremePortLoadshareTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 1)
)
if mibBuilder.loadTexts:
    extremePortLoadshareTable.setStatus("deprecated")
_ExtremePortLoadshareEntry_Object = MibTableRow
extremePortLoadshareEntry = _ExtremePortLoadshareEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 1, 1)
)
extremePortLoadshareEntry.setIndexNames(
    (0, "EXTREME-PORT-MIB", "extremePortLoadshareMasterIfIndex"),
    (0, "EXTREME-PORT-MIB", "extremePortLoadshareSlaveIfIndex"),
)
if mibBuilder.loadTexts:
    extremePortLoadshareEntry.setStatus("deprecated")


class _ExtremePortLoadshareMasterIfIndex_Type(Integer32):
    """Custom type extremePortLoadshareMasterIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremePortLoadshareMasterIfIndex_Type.__name__ = "Integer32"
_ExtremePortLoadshareMasterIfIndex_Object = MibTableColumn
extremePortLoadshareMasterIfIndex = _ExtremePortLoadshareMasterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 1, 1, 1),
    _ExtremePortLoadshareMasterIfIndex_Type()
)
extremePortLoadshareMasterIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremePortLoadshareMasterIfIndex.setStatus("deprecated")


class _ExtremePortLoadshareSlaveIfIndex_Type(Integer32):
    """Custom type extremePortLoadshareSlaveIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremePortLoadshareSlaveIfIndex_Type.__name__ = "Integer32"
_ExtremePortLoadshareSlaveIfIndex_Object = MibTableColumn
extremePortLoadshareSlaveIfIndex = _ExtremePortLoadshareSlaveIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 1, 1, 2),
    _ExtremePortLoadshareSlaveIfIndex_Type()
)
extremePortLoadshareSlaveIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremePortLoadshareSlaveIfIndex.setStatus("deprecated")


class _ExtremePortLoadshareGrouping_Type(Integer32):
    """Custom type extremePortLoadshareGrouping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("pair", 2),
          ("quad", 4))
    )


_ExtremePortLoadshareGrouping_Type.__name__ = "Integer32"
_ExtremePortLoadshareGrouping_Object = MibTableColumn
extremePortLoadshareGrouping = _ExtremePortLoadshareGrouping_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 1, 1, 3),
    _ExtremePortLoadshareGrouping_Type()
)
extremePortLoadshareGrouping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremePortLoadshareGrouping.setStatus("deprecated")
_ExtremePortLoadshareStatus_Type = RowStatus
_ExtremePortLoadshareStatus_Object = MibTableColumn
extremePortLoadshareStatus = _ExtremePortLoadshareStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 1, 1, 4),
    _ExtremePortLoadshareStatus_Type()
)
extremePortLoadshareStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremePortLoadshareStatus.setStatus("deprecated")
_ExtremePortSummitlinkTable_Object = MibTable
extremePortSummitlinkTable = _ExtremePortSummitlinkTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 2)
)
if mibBuilder.loadTexts:
    extremePortSummitlinkTable.setStatus("deprecated")
_ExtremePortSummitlinkEntry_Object = MibTableRow
extremePortSummitlinkEntry = _ExtremePortSummitlinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 2, 1)
)
extremePortSummitlinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremePortSummitlinkEntry.setStatus("deprecated")


class _ExtremePortSummitlinkAdminMode_Type(Integer32):
    """Custom type extremePortSummitlinkAdminMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernetOnly", 1),
          ("summitlinkOnly", 2))
    )


_ExtremePortSummitlinkAdminMode_Type.__name__ = "Integer32"
_ExtremePortSummitlinkAdminMode_Object = MibTableColumn
extremePortSummitlinkAdminMode = _ExtremePortSummitlinkAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 2, 1, 1),
    _ExtremePortSummitlinkAdminMode_Type()
)
extremePortSummitlinkAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremePortSummitlinkAdminMode.setStatus("deprecated")


class _ExtremePortSummitlinkOperMode_Type(Integer32):
    """Custom type extremePortSummitlinkOperMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernetOnly", 1),
          ("summitlinkOnly", 2))
    )


_ExtremePortSummitlinkOperMode_Type.__name__ = "Integer32"
_ExtremePortSummitlinkOperMode_Object = MibTableColumn
extremePortSummitlinkOperMode = _ExtremePortSummitlinkOperMode_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 2, 1, 2),
    _ExtremePortSummitlinkOperMode_Type()
)
extremePortSummitlinkOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortSummitlinkOperMode.setStatus("deprecated")


class _ExtremePortSummitlinkState_Type(Integer32):
    """Custom type extremePortSummitlinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_ExtremePortSummitlinkState_Type.__name__ = "Integer32"
_ExtremePortSummitlinkState_Object = MibTableColumn
extremePortSummitlinkState = _ExtremePortSummitlinkState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 2, 1, 3),
    _ExtremePortSummitlinkState_Type()
)
extremePortSummitlinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortSummitlinkState.setStatus("deprecated")


class _ExtremePortSummitlinkRejectReason_Type(Integer32):
    """Custom type extremePortSummitlinkRejectReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("other", 2),
          ("stackMisconnected", 3))
    )


_ExtremePortSummitlinkRejectReason_Type.__name__ = "Integer32"
_ExtremePortSummitlinkRejectReason_Object = MibTableColumn
extremePortSummitlinkRejectReason = _ExtremePortSummitlinkRejectReason_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 2, 1, 4),
    _ExtremePortSummitlinkRejectReason_Type()
)
extremePortSummitlinkRejectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortSummitlinkRejectReason.setStatus("deprecated")
_ExtremePortLoadshare2Table_Object = MibTable
extremePortLoadshare2Table = _ExtremePortLoadshare2Table_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 3)
)
if mibBuilder.loadTexts:
    extremePortLoadshare2Table.setStatus("current")
_ExtremePortLoadshare2Entry_Object = MibTableRow
extremePortLoadshare2Entry = _ExtremePortLoadshare2Entry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 3, 1)
)
extremePortLoadshare2Entry.setIndexNames(
    (0, "EXTREME-PORT-MIB", "extremePortLoadshare2MasterIfIndex"),
    (0, "EXTREME-PORT-MIB", "extremePortLoadshare2SlaveIfIndex"),
)
if mibBuilder.loadTexts:
    extremePortLoadshare2Entry.setStatus("current")


class _ExtremePortLoadshare2MasterIfIndex_Type(Integer32):
    """Custom type extremePortLoadshare2MasterIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExtremePortLoadshare2MasterIfIndex_Type.__name__ = "Integer32"
_ExtremePortLoadshare2MasterIfIndex_Object = MibTableColumn
extremePortLoadshare2MasterIfIndex = _ExtremePortLoadshare2MasterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 3, 1, 1),
    _ExtremePortLoadshare2MasterIfIndex_Type()
)
extremePortLoadshare2MasterIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremePortLoadshare2MasterIfIndex.setStatus("current")


class _ExtremePortLoadshare2SlaveIfIndex_Type(Integer32):
    """Custom type extremePortLoadshare2SlaveIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExtremePortLoadshare2SlaveIfIndex_Type.__name__ = "Integer32"
_ExtremePortLoadshare2SlaveIfIndex_Object = MibTableColumn
extremePortLoadshare2SlaveIfIndex = _ExtremePortLoadshare2SlaveIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 3, 1, 2),
    _ExtremePortLoadshare2SlaveIfIndex_Type()
)
extremePortLoadshare2SlaveIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremePortLoadshare2SlaveIfIndex.setStatus("current")


class _ExtremePortLoadshare2Algorithm_Type(Integer32):
    """Custom type extremePortLoadshare2Algorithm based on Integer32"""
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
        *(("ingressPortOffset", 1),
          ("hash", 2),
          ("roundRobin", 3),
          ("l2Address", 4),
          ("l3Address", 5),
          ("l3l4Address", 6),
          ("customAddress", 7))
    )


_ExtremePortLoadshare2Algorithm_Type.__name__ = "Integer32"
_ExtremePortLoadshare2Algorithm_Object = MibTableColumn
extremePortLoadshare2Algorithm = _ExtremePortLoadshare2Algorithm_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 3, 1, 3),
    _ExtremePortLoadshare2Algorithm_Type()
)
extremePortLoadshare2Algorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremePortLoadshare2Algorithm.setStatus("current")
_ExtremePortLoadshare2Status_Type = RowStatus
_ExtremePortLoadshare2Status_Object = MibTableColumn
extremePortLoadshare2Status = _ExtremePortLoadshare2Status_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 3, 1, 4),
    _ExtremePortLoadshare2Status_Type()
)
extremePortLoadshare2Status.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremePortLoadshare2Status.setStatus("current")


class _ExtremePortLoadshare2MinActiveLinks_Type(Unsigned32):
    """Custom type extremePortLoadshare2MinActiveLinks based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ExtremePortLoadshare2MinActiveLinks_Type.__name__ = "Unsigned32"
_ExtremePortLoadshare2MinActiveLinks_Object = MibTableColumn
extremePortLoadshare2MinActiveLinks = _ExtremePortLoadshare2MinActiveLinks_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 3, 1, 5),
    _ExtremePortLoadshare2MinActiveLinks_Type()
)
extremePortLoadshare2MinActiveLinks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremePortLoadshare2MinActiveLinks.setStatus("current")


class _ExtremePortLoadshare2AggControlType_Type(Integer32):
    """Custom type extremePortLoadshare2AggControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("lacp", 2),
          ("healthcheck", 3))
    )


_ExtremePortLoadshare2AggControlType_Type.__name__ = "Integer32"
_ExtremePortLoadshare2AggControlType_Object = MibTableColumn
extremePortLoadshare2AggControlType = _ExtremePortLoadshare2AggControlType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 3, 1, 6),
    _ExtremePortLoadshare2AggControlType_Type()
)
extremePortLoadshare2AggControlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremePortLoadshare2AggControlType.setStatus("current")
_ExtremePortRateShapeTable_Object = MibTable
extremePortRateShapeTable = _ExtremePortRateShapeTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 4)
)
if mibBuilder.loadTexts:
    extremePortRateShapeTable.setStatus("current")
_ExtremePortRateShapeEntry_Object = MibTableRow
extremePortRateShapeEntry = _ExtremePortRateShapeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 4, 1)
)
extremePortRateShapeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "EXTREME-VLAN-MIB", "extremeVlanIfIndex"),
)
if mibBuilder.loadTexts:
    extremePortRateShapeEntry.setStatus("current")


class _ExtremePortRateShapePortType_Type(Integer32):
    """Custom type extremePortRateShapePortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rateLimited", 1),
          ("loopBack", 2))
    )


_ExtremePortRateShapePortType_Type.__name__ = "Integer32"
_ExtremePortRateShapePortType_Object = MibTableColumn
extremePortRateShapePortType = _ExtremePortRateShapePortType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 4, 1, 1),
    _ExtremePortRateShapePortType_Type()
)
extremePortRateShapePortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremePortRateShapePortType.setStatus("current")


class _ExtremePortRateShapeLoopbackTag_Type(Integer32):
    """Custom type extremePortRateShapeLoopbackTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_ExtremePortRateShapeLoopbackTag_Type.__name__ = "Integer32"
_ExtremePortRateShapeLoopbackTag_Object = MibTableColumn
extremePortRateShapeLoopbackTag = _ExtremePortRateShapeLoopbackTag_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 4, 1, 2),
    _ExtremePortRateShapeLoopbackTag_Type()
)
extremePortRateShapeLoopbackTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremePortRateShapeLoopbackTag.setStatus("current")
_ExtremePortRateShapeStatus_Type = RowStatus
_ExtremePortRateShapeStatus_Object = MibTableColumn
extremePortRateShapeStatus = _ExtremePortRateShapeStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 4, 1, 3),
    _ExtremePortRateShapeStatus_Type()
)
extremePortRateShapeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremePortRateShapeStatus.setStatus("current")
_ExtremePortUtilizationTable_Object = MibTable
extremePortUtilizationTable = _ExtremePortUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 5)
)
if mibBuilder.loadTexts:
    extremePortUtilizationTable.setStatus("current")
_ExtremePortUtilizationEntry_Object = MibTableRow
extremePortUtilizationEntry = _ExtremePortUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 5, 1)
)
extremePortUtilizationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremePortUtilizationEntry.setStatus("current")
_ExtremePortUtilizationAvgTxBw_Type = Integer32
_ExtremePortUtilizationAvgTxBw_Object = MibTableColumn
extremePortUtilizationAvgTxBw = _ExtremePortUtilizationAvgTxBw_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 5, 1, 1),
    _ExtremePortUtilizationAvgTxBw_Type()
)
extremePortUtilizationAvgTxBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortUtilizationAvgTxBw.setStatus("current")
_ExtremePortUtilizationAvgRxBw_Type = Integer32
_ExtremePortUtilizationAvgRxBw_Object = MibTableColumn
extremePortUtilizationAvgRxBw = _ExtremePortUtilizationAvgRxBw_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 5, 1, 2),
    _ExtremePortUtilizationAvgRxBw_Type()
)
extremePortUtilizationAvgRxBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortUtilizationAvgRxBw.setStatus("current")
_ExtremePortUtilizationPeakTxBw_Type = Integer32
_ExtremePortUtilizationPeakTxBw_Object = MibTableColumn
extremePortUtilizationPeakTxBw = _ExtremePortUtilizationPeakTxBw_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 5, 1, 3),
    _ExtremePortUtilizationPeakTxBw_Type()
)
extremePortUtilizationPeakTxBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortUtilizationPeakTxBw.setStatus("current")
_ExtremePortUtilizationPeakRxBw_Type = Integer32
_ExtremePortUtilizationPeakRxBw_Object = MibTableColumn
extremePortUtilizationPeakRxBw = _ExtremePortUtilizationPeakRxBw_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 5, 1, 4),
    _ExtremePortUtilizationPeakRxBw_Type()
)
extremePortUtilizationPeakRxBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortUtilizationPeakRxBw.setStatus("current")
_ExtremePortInfoTable_Object = MibTable
extremePortInfoTable = _ExtremePortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 6)
)
if mibBuilder.loadTexts:
    extremePortInfoTable.setStatus("current")
_ExtremePortInfoEntry_Object = MibTableRow
extremePortInfoEntry = _ExtremePortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 6, 1)
)
extremePortInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremePortInfoEntry.setStatus("current")
_ExtremePortInfoFilterUpCounter_Type = Counter32
_ExtremePortInfoFilterUpCounter_Object = MibTableColumn
extremePortInfoFilterUpCounter = _ExtremePortInfoFilterUpCounter_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 6, 1, 1),
    _ExtremePortInfoFilterUpCounter_Type()
)
extremePortInfoFilterUpCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortInfoFilterUpCounter.setStatus("current")
_ExtremePortInfoFilterDownCounter_Type = Counter32
_ExtremePortInfoFilterDownCounter_Object = MibTableColumn
extremePortInfoFilterDownCounter = _ExtremePortInfoFilterDownCounter_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 6, 1, 2),
    _ExtremePortInfoFilterDownCounter_Type()
)
extremePortInfoFilterDownCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortInfoFilterDownCounter.setStatus("current")
_ExtremePortXenpakVendorTable_Object = MibTable
extremePortXenpakVendorTable = _ExtremePortXenpakVendorTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 7)
)
if mibBuilder.loadTexts:
    extremePortXenpakVendorTable.setStatus("current")
_ExtremePortXenpakVendorEntry_Object = MibTableRow
extremePortXenpakVendorEntry = _ExtremePortXenpakVendorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 7, 1)
)
extremePortXenpakVendorEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremePortXenpakVendorEntry.setStatus("current")


class _ExtremePortXenpakVendorName_Type(DisplayString):
    """Custom type extremePortXenpakVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_ExtremePortXenpakVendorName_Type.__name__ = "DisplayString"
_ExtremePortXenpakVendorName_Object = MibTableColumn
extremePortXenpakVendorName = _ExtremePortXenpakVendorName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 7, 1, 1),
    _ExtremePortXenpakVendorName_Type()
)
extremePortXenpakVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortXenpakVendorName.setStatus("current")
_ExtremePortIngressStats_ObjectIdentity = ObjectIdentity
extremePortIngressStats = _ExtremePortIngressStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 8)
)
_ExtremePortIngressStatsPortTable_Object = MibTable
extremePortIngressStatsPortTable = _ExtremePortIngressStatsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 1)
)
if mibBuilder.loadTexts:
    extremePortIngressStatsPortTable.setStatus("current")
_ExtremePortIngressPortStatsEntry_Object = MibTableRow
extremePortIngressPortStatsEntry = _ExtremePortIngressPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 1, 1)
)
extremePortIngressPortStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremePortIngressPortStatsEntry.setStatus("current")


class _ExtremePortIngressStatsLinkStatus_Type(Integer32):
    """Custom type extremePortIngressStatsLinkStatus based on Integer32"""
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
        *(("ready", 1),
          ("active", 2),
          ("disabled", 3),
          ("notPresent", 4))
    )


_ExtremePortIngressStatsLinkStatus_Type.__name__ = "Integer32"
_ExtremePortIngressStatsLinkStatus_Object = MibTableColumn
extremePortIngressStatsLinkStatus = _ExtremePortIngressStatsLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 1, 1, 1),
    _ExtremePortIngressStatsLinkStatus_Type()
)
extremePortIngressStatsLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortIngressStatsLinkStatus.setStatus("current")
_ExtremePortIngressStatsPortHighPriBytes_Type = Counter64
_ExtremePortIngressStatsPortHighPriBytes_Object = MibTableColumn
extremePortIngressStatsPortHighPriBytes = _ExtremePortIngressStatsPortHighPriBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 1, 1, 2),
    _ExtremePortIngressStatsPortHighPriBytes_Type()
)
extremePortIngressStatsPortHighPriBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortIngressStatsPortHighPriBytes.setStatus("current")
_ExtremePortIngressStatsPortLowPriBytes_Type = Counter64
_ExtremePortIngressStatsPortLowPriBytes_Object = MibTableColumn
extremePortIngressStatsPortLowPriBytes = _ExtremePortIngressStatsPortLowPriBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 1, 1, 3),
    _ExtremePortIngressStatsPortLowPriBytes_Type()
)
extremePortIngressStatsPortLowPriBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortIngressStatsPortLowPriBytes.setStatus("current")
_ExtremePortIngressStatsPortDroppedBytes_Type = Counter64
_ExtremePortIngressStatsPortDroppedBytes_Object = MibTableColumn
extremePortIngressStatsPortDroppedBytes = _ExtremePortIngressStatsPortDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 1, 1, 4),
    _ExtremePortIngressStatsPortDroppedBytes_Type()
)
extremePortIngressStatsPortDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortIngressStatsPortDroppedBytes.setStatus("current")
_ExtremePortIngressStatsTxXoff_Type = Counter64
_ExtremePortIngressStatsTxXoff_Object = MibTableColumn
extremePortIngressStatsTxXoff = _ExtremePortIngressStatsTxXoff_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 1, 1, 5),
    _ExtremePortIngressStatsTxXoff_Type()
)
extremePortIngressStatsTxXoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortIngressStatsTxXoff.setStatus("current")
_ExtremePortIngressStatsQueueTable_Object = MibTable
extremePortIngressStatsQueueTable = _ExtremePortIngressStatsQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 2)
)
if mibBuilder.loadTexts:
    extremePortIngressStatsQueueTable.setStatus("current")
_ExtremePortIngressQueueStatsEntry_Object = MibTableRow
extremePortIngressQueueStatsEntry = _ExtremePortIngressQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 2, 1)
)
extremePortIngressQueueStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "EXTREME-PORT-MIB", "extremePortIngressStatsQueueIndex"),
)
if mibBuilder.loadTexts:
    extremePortIngressQueueStatsEntry.setStatus("current")
_ExtremePortIngressStatsQueueIndex_Type = Integer32
_ExtremePortIngressStatsQueueIndex_Object = MibTableColumn
extremePortIngressStatsQueueIndex = _ExtremePortIngressStatsQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 2, 1, 1),
    _ExtremePortIngressStatsQueueIndex_Type()
)
extremePortIngressStatsQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortIngressStatsQueueIndex.setStatus("current")
_ExtremePortIngressStatsQueueHighPriBytes_Type = Counter64
_ExtremePortIngressStatsQueueHighPriBytes_Object = MibTableColumn
extremePortIngressStatsQueueHighPriBytes = _ExtremePortIngressStatsQueueHighPriBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 2, 1, 2),
    _ExtremePortIngressStatsQueueHighPriBytes_Type()
)
extremePortIngressStatsQueueHighPriBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortIngressStatsQueueHighPriBytes.setStatus("current")
_ExtremePortIngressStatsQueueLowPriBytes_Type = Counter64
_ExtremePortIngressStatsQueueLowPriBytes_Object = MibTableColumn
extremePortIngressStatsQueueLowPriBytes = _ExtremePortIngressStatsQueueLowPriBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 2, 1, 3),
    _ExtremePortIngressStatsQueueLowPriBytes_Type()
)
extremePortIngressStatsQueueLowPriBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortIngressStatsQueueLowPriBytes.setStatus("current")
_ExtremePortIngressStatsQueuePercentDropped_Type = Integer32
_ExtremePortIngressStatsQueuePercentDropped_Object = MibTableColumn
extremePortIngressStatsQueuePercentDropped = _ExtremePortIngressStatsQueuePercentDropped_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 2, 1, 4),
    _ExtremePortIngressStatsQueuePercentDropped_Type()
)
extremePortIngressStatsQueuePercentDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortIngressStatsQueuePercentDropped.setStatus("current")
_ExtremePortEgressRateLimitTable_Object = MibTable
extremePortEgressRateLimitTable = _ExtremePortEgressRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 9)
)
if mibBuilder.loadTexts:
    extremePortEgressRateLimitTable.setStatus("current")
_ExtremePortEgressRateLimitEntry_Object = MibTableRow
extremePortEgressRateLimitEntry = _ExtremePortEgressRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 9, 1)
)
extremePortEgressRateLimitEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremePortEgressRateLimitEntry.setStatus("current")


class _ExtremePortEgressRateLimitType_Type(Integer32):
    """Custom type extremePortEgressRateLimitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("percentage", 1),
          ("kbps", 2),
          ("mbps", 3))
    )


_ExtremePortEgressRateLimitType_Type.__name__ = "Integer32"
_ExtremePortEgressRateLimitType_Object = MibTableColumn
extremePortEgressRateLimitType = _ExtremePortEgressRateLimitType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 9, 1, 1),
    _ExtremePortEgressRateLimitType_Type()
)
extremePortEgressRateLimitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortEgressRateLimitType.setStatus("current")
_ExtremePortEgressRateLimitValue_Type = Integer32
_ExtremePortEgressRateLimitValue_Object = MibTableColumn
extremePortEgressRateLimitValue = _ExtremePortEgressRateLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 9, 1, 2),
    _ExtremePortEgressRateLimitValue_Type()
)
extremePortEgressRateLimitValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortEgressRateLimitValue.setStatus("current")
_ExtremeWiredClientTable_Object = MibTable
extremeWiredClientTable = _ExtremeWiredClientTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 10)
)
if mibBuilder.loadTexts:
    extremeWiredClientTable.setStatus("current")
_ExtremeWiredClientEntry_Object = MibTableRow
extremeWiredClientEntry = _ExtremeWiredClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 10, 1)
)
extremeWiredClientEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "EXTREME-PORT-MIB", "extremeWiredClientID"),
)
if mibBuilder.loadTexts:
    extremeWiredClientEntry.setStatus("current")
_ExtremeWiredClientID_Type = MacAddress
_ExtremeWiredClientID_Object = MibTableColumn
extremeWiredClientID = _ExtremeWiredClientID_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 10, 1, 1),
    _ExtremeWiredClientID_Type()
)
extremeWiredClientID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWiredClientID.setStatus("current")


class _ExtremeWiredClientState_Type(Integer32):
    """Custom type extremeWiredClientState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authenticated", 1),
          ("unauthenticated", 2))
    )


_ExtremeWiredClientState_Type.__name__ = "Integer32"
_ExtremeWiredClientState_Object = MibTableColumn
extremeWiredClientState = _ExtremeWiredClientState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 10, 1, 2),
    _ExtremeWiredClientState_Type()
)
extremeWiredClientState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWiredClientState.setStatus("current")
_ExtremeWiredClientVLAN_Type = Integer32
_ExtremeWiredClientVLAN_Object = MibTableColumn
extremeWiredClientVLAN = _ExtremeWiredClientVLAN_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 10, 1, 3),
    _ExtremeWiredClientVLAN_Type()
)
extremeWiredClientVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWiredClientVLAN.setStatus("current")
_ExtremeWiredClientPriority_Type = Integer32
_ExtremeWiredClientPriority_Object = MibTableColumn
extremeWiredClientPriority = _ExtremeWiredClientPriority_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 10, 1, 4),
    _ExtremeWiredClientPriority_Type()
)
extremeWiredClientPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWiredClientPriority.setStatus("current")
_ExtremeWiredClientAuthType_Type = ClientAuthType
_ExtremeWiredClientAuthType_Object = MibTableColumn
extremeWiredClientAuthType = _ExtremeWiredClientAuthType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 10, 1, 5),
    _ExtremeWiredClientAuthType_Type()
)
extremeWiredClientAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWiredClientAuthType.setStatus("current")
_ExtremeWiredClientLastStateChangeTime_Type = TimeTicks
_ExtremeWiredClientLastStateChangeTime_Object = MibTableColumn
extremeWiredClientLastStateChangeTime = _ExtremeWiredClientLastStateChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 10, 1, 6),
    _ExtremeWiredClientLastStateChangeTime_Type()
)
extremeWiredClientLastStateChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWiredClientLastStateChangeTime.setStatus("current")
_ExtremeWiredClientIP_Type = IpAddress
_ExtremeWiredClientIP_Object = MibTableColumn
extremeWiredClientIP = _ExtremeWiredClientIP_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 10, 1, 7),
    _ExtremeWiredClientIP_Type()
)
extremeWiredClientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWiredClientIP.setStatus("current")
_ExtremePortUtilizationExtnTable_Object = MibTable
extremePortUtilizationExtnTable = _ExtremePortUtilizationExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 11)
)
if mibBuilder.loadTexts:
    extremePortUtilizationExtnTable.setStatus("current")
_ExtremePortUtilizationExtnEntry_Object = MibTableRow
extremePortUtilizationExtnEntry = _ExtremePortUtilizationExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 11, 1)
)
extremePortUtilizationExtnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremePortUtilizationExtnEntry.setStatus("current")
_ExtremePortUtilizationAvgTxPkts_Type = Integer32
_ExtremePortUtilizationAvgTxPkts_Object = MibTableColumn
extremePortUtilizationAvgTxPkts = _ExtremePortUtilizationAvgTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 11, 1, 1),
    _ExtremePortUtilizationAvgTxPkts_Type()
)
extremePortUtilizationAvgTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortUtilizationAvgTxPkts.setStatus("current")
_ExtremePortUtilizationAvgRxPkts_Type = Integer32
_ExtremePortUtilizationAvgRxPkts_Object = MibTableColumn
extremePortUtilizationAvgRxPkts = _ExtremePortUtilizationAvgRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 11, 1, 2),
    _ExtremePortUtilizationAvgRxPkts_Type()
)
extremePortUtilizationAvgRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortUtilizationAvgRxPkts.setStatus("current")
_ExtremePortUtilizationPeakTxPkts_Type = Integer32
_ExtremePortUtilizationPeakTxPkts_Object = MibTableColumn
extremePortUtilizationPeakTxPkts = _ExtremePortUtilizationPeakTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 11, 1, 3),
    _ExtremePortUtilizationPeakTxPkts_Type()
)
extremePortUtilizationPeakTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortUtilizationPeakTxPkts.setStatus("current")
_ExtremePortUtilizationPeakRxPkts_Type = Integer32
_ExtremePortUtilizationPeakRxPkts_Object = MibTableColumn
extremePortUtilizationPeakRxPkts = _ExtremePortUtilizationPeakRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 11, 1, 4),
    _ExtremePortUtilizationPeakRxPkts_Type()
)
extremePortUtilizationPeakRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortUtilizationPeakRxPkts.setStatus("current")
_ExtremePortUtilizationAvgTxBytes_Type = Integer32
_ExtremePortUtilizationAvgTxBytes_Object = MibTableColumn
extremePortUtilizationAvgTxBytes = _ExtremePortUtilizationAvgTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 11, 1, 5),
    _ExtremePortUtilizationAvgTxBytes_Type()
)
extremePortUtilizationAvgTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortUtilizationAvgTxBytes.setStatus("current")
_ExtremePortUtilizationAvgRxBytes_Type = Integer32
_ExtremePortUtilizationAvgRxBytes_Object = MibTableColumn
extremePortUtilizationAvgRxBytes = _ExtremePortUtilizationAvgRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 11, 1, 6),
    _ExtremePortUtilizationAvgRxBytes_Type()
)
extremePortUtilizationAvgRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortUtilizationAvgRxBytes.setStatus("current")
_ExtremePortUtilizationPeakTxBytes_Type = Integer32
_ExtremePortUtilizationPeakTxBytes_Object = MibTableColumn
extremePortUtilizationPeakTxBytes = _ExtremePortUtilizationPeakTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 11, 1, 7),
    _ExtremePortUtilizationPeakTxBytes_Type()
)
extremePortUtilizationPeakTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortUtilizationPeakTxBytes.setStatus("current")
_ExtremePortUtilizationPeakRxBytes_Type = Integer32
_ExtremePortUtilizationPeakRxBytes_Object = MibTableColumn
extremePortUtilizationPeakRxBytes = _ExtremePortUtilizationPeakRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 11, 1, 8),
    _ExtremePortUtilizationPeakRxBytes_Type()
)
extremePortUtilizationPeakRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortUtilizationPeakRxBytes.setStatus("current")
_ExtremePortQosStatsTable_Object = MibTable
extremePortQosStatsTable = _ExtremePortQosStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 12)
)
if mibBuilder.loadTexts:
    extremePortQosStatsTable.setStatus("current")
_ExtremePortQosStatsEntry_Object = MibTableRow
extremePortQosStatsEntry = _ExtremePortQosStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 12, 1)
)
extremePortQosStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "EXTREME-PORT-MIB", "extremePortQosIngress"),
)
if mibBuilder.loadTexts:
    extremePortQosStatsEntry.setStatus("current")
_ExtremePortQosIngress_Type = ExtremePortTrafficDirection
_ExtremePortQosIngress_Object = MibTableColumn
extremePortQosIngress = _ExtremePortQosIngress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 12, 1, 1),
    _ExtremePortQosIngress_Type()
)
extremePortQosIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortQosIngress.setStatus("current")
_ExtremePortQP0TxBytes_Type = Counter64
_ExtremePortQP0TxBytes_Object = MibTableColumn
extremePortQP0TxBytes = _ExtremePortQP0TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 12, 1, 2),
    _ExtremePortQP0TxBytes_Type()
)
extremePortQP0TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortQP0TxBytes.setStatus("current")
_ExtremePortQP0TxPkts_Type = Counter64
_ExtremePortQP0TxPkts_Object = MibTableColumn
extremePortQP0TxPkts = _ExtremePortQP0TxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 12, 1, 3),
    _ExtremePortQP0TxPkts_Type()
)
extremePortQP0TxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortQP0TxPkts.setStatus("current")
_ExtremePortQP1TxBytes_Type = Counter64
_ExtremePortQP1TxBytes_Object = MibTableColumn
extremePortQP1TxBytes = _ExtremePortQP1TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 12, 1, 4),
    _ExtremePortQP1TxBytes_Type()
)
extremePortQP1TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortQP1TxBytes.setStatus("current")
_ExtremePortQP1TxPkts_Type = Counter64
_ExtremePortQP1TxPkts_Object = MibTableColumn
extremePortQP1TxPkts = _ExtremePortQP1TxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 12, 1, 5),
    _ExtremePortQP1TxPkts_Type()
)
extremePortQP1TxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortQP1TxPkts.setStatus("current")
_ExtremePortQP2TxBytes_Type = Counter64
_ExtremePortQP2TxBytes_Object = MibTableColumn
extremePortQP2TxBytes = _ExtremePortQP2TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 12, 1, 6),
    _ExtremePortQP2TxBytes_Type()
)
extremePortQP2TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortQP2TxBytes.setStatus("current")
_ExtremePortQP2TxPkts_Type = Counter64
_ExtremePortQP2TxPkts_Object = MibTableColumn
extremePortQP2TxPkts = _ExtremePortQP2TxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 12, 1, 7),
    _ExtremePortQP2TxPkts_Type()
)
extremePortQP2TxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortQP2TxPkts.setStatus("current")
_ExtremePortQP3TxBytes_Type = Counter64
_ExtremePortQP3TxBytes_Object = MibTableColumn
extremePortQP3TxBytes = _ExtremePortQP3TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 12, 1, 8),
    _ExtremePortQP3TxBytes_Type()
)
extremePortQP3TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortQP3TxBytes.setStatus("current")
_ExtremePortQP3TxPkts_Type = Counter64
_ExtremePortQP3TxPkts_Object = MibTableColumn
extremePortQP3TxPkts = _ExtremePortQP3TxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 12, 1, 9),
    _ExtremePortQP3TxPkts_Type()
)
extremePortQP3TxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortQP3TxPkts.setStatus("current")
_ExtremePortQP4TxBytes_Type = Counter64
_ExtremePortQP4TxBytes_Object = MibTableColumn
extremePortQP4TxBytes = _ExtremePortQP4TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 12, 1, 10),
    _ExtremePortQP4TxBytes_Type()
)
extremePortQP4TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortQP4TxBytes.setStatus("current")
_ExtremePortQP4TxPkts_Type = Counter64
_ExtremePortQP4TxPkts_Object = MibTableColumn
extremePortQP4TxPkts = _ExtremePortQP4TxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 12, 1, 11),
    _ExtremePortQP4TxPkts_Type()
)
extremePortQP4TxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortQP4TxPkts.setStatus("current")
_ExtremePortQP5TxBytes_Type = Counter64
_ExtremePortQP5TxBytes_Object = MibTableColumn
extremePortQP5TxBytes = _ExtremePortQP5TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 12, 1, 12),
    _ExtremePortQP5TxBytes_Type()
)
extremePortQP5TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortQP5TxBytes.setStatus("current")
_ExtremePortQP5TxPkts_Type = Counter64
_ExtremePortQP5TxPkts_Object = MibTableColumn
extremePortQP5TxPkts = _ExtremePortQP5TxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 12, 1, 13),
    _ExtremePortQP5TxPkts_Type()
)
extremePortQP5TxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortQP5TxPkts.setStatus("current")
_ExtremePortQP6TxBytes_Type = Counter64
_ExtremePortQP6TxBytes_Object = MibTableColumn
extremePortQP6TxBytes = _ExtremePortQP6TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 12, 1, 14),
    _ExtremePortQP6TxBytes_Type()
)
extremePortQP6TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortQP6TxBytes.setStatus("current")
_ExtremePortQP6TxPkts_Type = Counter64
_ExtremePortQP6TxPkts_Object = MibTableColumn
extremePortQP6TxPkts = _ExtremePortQP6TxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 12, 1, 15),
    _ExtremePortQP6TxPkts_Type()
)
extremePortQP6TxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortQP6TxPkts.setStatus("current")
_ExtremePortQP7TxBytes_Type = Counter64
_ExtremePortQP7TxBytes_Object = MibTableColumn
extremePortQP7TxBytes = _ExtremePortQP7TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 12, 1, 16),
    _ExtremePortQP7TxBytes_Type()
)
extremePortQP7TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortQP7TxBytes.setStatus("current")
_ExtremePortQP7TxPkts_Type = Counter64
_ExtremePortQP7TxPkts_Object = MibTableColumn
extremePortQP7TxPkts = _ExtremePortQP7TxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 12, 1, 17),
    _ExtremePortQP7TxPkts_Type()
)
extremePortQP7TxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortQP7TxPkts.setStatus("current")
_ExtremePortMau_ObjectIdentity = ObjectIdentity
extremePortMau = _ExtremePortMau_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 13)
)
_ExtremePortMauTable_Object = MibTable
extremePortMauTable = _ExtremePortMauTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 13, 1)
)
if mibBuilder.loadTexts:
    extremePortMauTable.setStatus("current")
_ExtremePortMauEntry_Object = MibTableRow
extremePortMauEntry = _ExtremePortMauEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 13, 1, 1)
)
extremePortMauEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremePortMauEntry.setStatus("current")


class _ExtremePortMauType_Type(DisplayString):
    """Custom type extremePortMauType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_ExtremePortMauType_Type.__name__ = "DisplayString"
_ExtremePortMauType_Object = MibTableColumn
extremePortMauType = _ExtremePortMauType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 13, 1, 1, 1),
    _ExtremePortMauType_Type()
)
extremePortMauType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortMauType.setStatus("current")


class _ExtremePortMauVendorName_Type(DisplayString):
    """Custom type extremePortMauVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_ExtremePortMauVendorName_Type.__name__ = "DisplayString"
_ExtremePortMauVendorName_Object = MibTableColumn
extremePortMauVendorName = _ExtremePortMauVendorName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 13, 1, 1, 2),
    _ExtremePortMauVendorName_Type()
)
extremePortMauVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortMauVendorName.setStatus("current")


class _ExtremePortMauStatus_Type(Integer32):
    """Custom type extremePortMauStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inserted", 1),
          ("empty", 2))
    )


_ExtremePortMauStatus_Type.__name__ = "Integer32"
_ExtremePortMauStatus_Object = MibTableColumn
extremePortMauStatus = _ExtremePortMauStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 13, 1, 1, 3),
    _ExtremePortMauStatus_Type()
)
extremePortMauStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortMauStatus.setStatus("current")


class _ExtremePortMauRestrict_Type(DisplayString):
    """Custom type extremePortMauRestrict based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_ExtremePortMauRestrict_Type.__name__ = "DisplayString"
_ExtremePortMauRestrict_Object = MibTableColumn
extremePortMauRestrict = _ExtremePortMauRestrict_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 13, 1, 1, 4),
    _ExtremePortMauRestrict_Type()
)
extremePortMauRestrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortMauRestrict.setStatus("current")
_ExtremePortMauTraps_ObjectIdentity = ObjectIdentity
extremePortMauTraps = _ExtremePortMauTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 13, 2)
)
_ExtremePortMauTrapsPrefix_ObjectIdentity = ObjectIdentity
extremePortMauTrapsPrefix = _ExtremePortMauTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 13, 2, 0)
)
_ExtremePortCongestionStatsTable_Object = MibTable
extremePortCongestionStatsTable = _ExtremePortCongestionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 14)
)
if mibBuilder.loadTexts:
    extremePortCongestionStatsTable.setStatus("current")
_ExtremePortCongestionStatsEntry_Object = MibTableRow
extremePortCongestionStatsEntry = _ExtremePortCongestionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 14, 1)
)
extremePortCongestionStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremePortCongestionStatsEntry.setStatus("current")
_ExtremePortCongDropPkts_Type = Counter64
_ExtremePortCongDropPkts_Object = MibTableColumn
extremePortCongDropPkts = _ExtremePortCongDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 14, 1, 1),
    _ExtremePortCongDropPkts_Type()
)
extremePortCongDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortCongDropPkts.setStatus("current")
_ExtremePortQosCongestionStatsTable_Object = MibTable
extremePortQosCongestionStatsTable = _ExtremePortQosCongestionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 15)
)
if mibBuilder.loadTexts:
    extremePortQosCongestionStatsTable.setStatus("current")
_ExtremePortQosCongestionStatsEntry_Object = MibTableRow
extremePortQosCongestionStatsEntry = _ExtremePortQosCongestionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 15, 1)
)
extremePortQosCongestionStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremePortQosCongestionStatsEntry.setStatus("current")
_ExtremePortQP0CongPkts_Type = Counter64
_ExtremePortQP0CongPkts_Object = MibTableColumn
extremePortQP0CongPkts = _ExtremePortQP0CongPkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 15, 1, 1),
    _ExtremePortQP0CongPkts_Type()
)
extremePortQP0CongPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortQP0CongPkts.setStatus("current")
_ExtremePortQP1CongPkts_Type = Counter64
_ExtremePortQP1CongPkts_Object = MibTableColumn
extremePortQP1CongPkts = _ExtremePortQP1CongPkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 15, 1, 2),
    _ExtremePortQP1CongPkts_Type()
)
extremePortQP1CongPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortQP1CongPkts.setStatus("current")
_ExtremePortQP2CongPkts_Type = Counter64
_ExtremePortQP2CongPkts_Object = MibTableColumn
extremePortQP2CongPkts = _ExtremePortQP2CongPkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 15, 1, 3),
    _ExtremePortQP2CongPkts_Type()
)
extremePortQP2CongPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortQP2CongPkts.setStatus("current")
_ExtremePortQP3CongPkts_Type = Counter64
_ExtremePortQP3CongPkts_Object = MibTableColumn
extremePortQP3CongPkts = _ExtremePortQP3CongPkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 15, 1, 4),
    _ExtremePortQP3CongPkts_Type()
)
extremePortQP3CongPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortQP3CongPkts.setStatus("current")
_ExtremePortQP4CongPkts_Type = Counter64
_ExtremePortQP4CongPkts_Object = MibTableColumn
extremePortQP4CongPkts = _ExtremePortQP4CongPkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 15, 1, 5),
    _ExtremePortQP4CongPkts_Type()
)
extremePortQP4CongPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortQP4CongPkts.setStatus("current")
_ExtremePortQP5CongPkts_Type = Counter64
_ExtremePortQP5CongPkts_Object = MibTableColumn
extremePortQP5CongPkts = _ExtremePortQP5CongPkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 15, 1, 6),
    _ExtremePortQP5CongPkts_Type()
)
extremePortQP5CongPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortQP5CongPkts.setStatus("current")
_ExtremePortQP6CongPkts_Type = Counter64
_ExtremePortQP6CongPkts_Object = MibTableColumn
extremePortQP6CongPkts = _ExtremePortQP6CongPkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 15, 1, 7),
    _ExtremePortQP6CongPkts_Type()
)
extremePortQP6CongPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortQP6CongPkts.setStatus("current")
_ExtremePortQP7CongPkts_Type = Counter64
_ExtremePortQP7CongPkts_Object = MibTableColumn
extremePortQP7CongPkts = _ExtremePortQP7CongPkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 15, 1, 8),
    _ExtremePortQP7CongPkts_Type()
)
extremePortQP7CongPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortQP7CongPkts.setStatus("current")
_ExtremePortVlanInfoTable_Object = MibTable
extremePortVlanInfoTable = _ExtremePortVlanInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 17)
)
if mibBuilder.loadTexts:
    extremePortVlanInfoTable.setStatus("current")
_ExtremePortVlanInfoEntry_Object = MibTableRow
extremePortVlanInfoEntry = _ExtremePortVlanInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 17, 1)
)
extremePortVlanInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "EXTREME-VLAN-MIB", "extremeVlanIfIndex"),
)
if mibBuilder.loadTexts:
    extremePortVlanInfoEntry.setStatus("current")


class _ExtremePortVlanInfoDescr_Type(DisplayString):
    """Custom type extremePortVlanInfoDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExtremePortVlanInfoDescr_Type.__name__ = "DisplayString"
_ExtremePortVlanInfoDescr_Object = MibTableColumn
extremePortVlanInfoDescr = _ExtremePortVlanInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 17, 1, 1),
    _ExtremePortVlanInfoDescr_Type()
)
extremePortVlanInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortVlanInfoDescr.setStatus("current")


class _ExtremePortVlanInfoLimitLearningEnabled_Type(Integer32):
    """Custom type extremePortVlanInfoLimitLearningEnabled based on Integer32"""
    defaultValue = 0


_ExtremePortVlanInfoLimitLearningEnabled_Type.__name__ = "Integer32"
_ExtremePortVlanInfoLimitLearningEnabled_Object = MibTableColumn
extremePortVlanInfoLimitLearningEnabled = _ExtremePortVlanInfoLimitLearningEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 17, 1, 2),
    _ExtremePortVlanInfoLimitLearningEnabled_Type()
)
extremePortVlanInfoLimitLearningEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremePortVlanInfoLimitLearningEnabled.setStatus("current")


class _ExtremePortVlanInfoLimitLearningNumber_Type(Integer32):
    """Custom type extremePortVlanInfoLimitLearningNumber based on Integer32"""
    defaultValue = 0


_ExtremePortVlanInfoLimitLearningNumber_Type.__name__ = "Integer32"
_ExtremePortVlanInfoLimitLearningNumber_Object = MibTableColumn
extremePortVlanInfoLimitLearningNumber = _ExtremePortVlanInfoLimitLearningNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 17, 1, 3),
    _ExtremePortVlanInfoLimitLearningNumber_Type()
)
extremePortVlanInfoLimitLearningNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremePortVlanInfoLimitLearningNumber.setStatus("current")


class _ExtremePortVlanInfoMacLockDownEnabled_Type(Integer32):
    """Custom type extremePortVlanInfoMacLockDownEnabled based on Integer32"""
    defaultValue = 0


_ExtremePortVlanInfoMacLockDownEnabled_Type.__name__ = "Integer32"
_ExtremePortVlanInfoMacLockDownEnabled_Object = MibTableColumn
extremePortVlanInfoMacLockDownEnabled = _ExtremePortVlanInfoMacLockDownEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 17, 1, 4),
    _ExtremePortVlanInfoMacLockDownEnabled_Type()
)
extremePortVlanInfoMacLockDownEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremePortVlanInfoMacLockDownEnabled.setStatus("current")
_ExtremePortConfigTable_Object = MibTable
extremePortConfigTable = _ExtremePortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 18)
)
if mibBuilder.loadTexts:
    extremePortConfigTable.setStatus("current")
_ExtremePortConfigEntry_Object = MibTableRow
extremePortConfigEntry = _ExtremePortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 18, 1)
)
extremePortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremePortConfigEntry.setStatus("current")


class _ExtremePortAutoNegotiation_Type(Integer32):
    """Custom type extremePortAutoNegotiation based on Integer32"""
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


_ExtremePortAutoNegotiation_Type.__name__ = "Integer32"
_ExtremePortAutoNegotiation_Object = MibTableColumn
extremePortAutoNegotiation = _ExtremePortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 18, 1, 1),
    _ExtremePortAutoNegotiation_Type()
)
extremePortAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremePortAutoNegotiation.setStatus("current")


class _ExtremePortAdminSpeed_Type(Integer32):
    """Custom type extremePortAdminSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("s10", 1),
          ("s100", 2),
          ("s1000", 3),
          ("s10000", 4),
          ("s25000", 5),
          ("s40000", 6),
          ("s50000", 7),
          ("s100000", 10),
          ("s2500", 11),
          ("s5000", 12))
    )


_ExtremePortAdminSpeed_Type.__name__ = "Integer32"
_ExtremePortAdminSpeed_Object = MibTableColumn
extremePortAdminSpeed = _ExtremePortAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 18, 1, 2),
    _ExtremePortAdminSpeed_Type()
)
extremePortAdminSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremePortAdminSpeed.setStatus("current")


class _ExtremePortDuplex_Type(Integer32):
    """Custom type extremePortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("half", 0),
          ("full", 1),
          ("auto", 2))
    )


_ExtremePortDuplex_Type.__name__ = "Integer32"
_ExtremePortDuplex_Object = MibTableColumn
extremePortDuplex = _ExtremePortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 18, 1, 3),
    _ExtremePortDuplex_Type()
)
extremePortDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremePortDuplex.setStatus("current")


class _ExtremePortMedium_Type(Integer32):
    """Custom type extremePortMedium based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copper", 0),
          ("fiber", 1),
          ("nonComboPort", 2))
    )


_ExtremePortMedium_Type.__name__ = "Integer32"
_ExtremePortMedium_Object = MibTableColumn
extremePortMedium = _ExtremePortMedium_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 18, 1, 4),
    _ExtremePortMedium_Type()
)
extremePortMedium.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremePortMedium.setStatus("current")

# Managed Objects groups


# Notification objects

extremePortMauChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 13, 2, 0, 1)
)
extremePortMauChangeTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("EXTREME-PORT-MIB", "extremePortMauType"),
        ("EXTREME-PORT-MIB", "extremePortMauStatus"))
)
if mibBuilder.loadTexts:
    extremePortMauChangeTrap.setStatus(
        "current"
    )

extremePortMauRestrictionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 13, 2, 0, 2)
)
extremePortMauRestrictionTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("EXTREME-PORT-MIB", "extremePortMauRestrict"))
)
if mibBuilder.loadTexts:
    extremePortMauRestrictionTrap.setStatus(
        "current"
    )

extremeRateLimitExceededAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 16)
)
extremeRateLimitExceededAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    extremeRateLimitExceededAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-PORT-MIB",
    **{"ExtremePortTrafficDirection": ExtremePortTrafficDirection,
       "extremePort": extremePort,
       "extremePortLoadshareTable": extremePortLoadshareTable,
       "extremePortLoadshareEntry": extremePortLoadshareEntry,
       "extremePortLoadshareMasterIfIndex": extremePortLoadshareMasterIfIndex,
       "extremePortLoadshareSlaveIfIndex": extremePortLoadshareSlaveIfIndex,
       "extremePortLoadshareGrouping": extremePortLoadshareGrouping,
       "extremePortLoadshareStatus": extremePortLoadshareStatus,
       "extremePortSummitlinkTable": extremePortSummitlinkTable,
       "extremePortSummitlinkEntry": extremePortSummitlinkEntry,
       "extremePortSummitlinkAdminMode": extremePortSummitlinkAdminMode,
       "extremePortSummitlinkOperMode": extremePortSummitlinkOperMode,
       "extremePortSummitlinkState": extremePortSummitlinkState,
       "extremePortSummitlinkRejectReason": extremePortSummitlinkRejectReason,
       "extremePortLoadshare2Table": extremePortLoadshare2Table,
       "extremePortLoadshare2Entry": extremePortLoadshare2Entry,
       "extremePortLoadshare2MasterIfIndex": extremePortLoadshare2MasterIfIndex,
       "extremePortLoadshare2SlaveIfIndex": extremePortLoadshare2SlaveIfIndex,
       "extremePortLoadshare2Algorithm": extremePortLoadshare2Algorithm,
       "extremePortLoadshare2Status": extremePortLoadshare2Status,
       "extremePortLoadshare2MinActiveLinks": extremePortLoadshare2MinActiveLinks,
       "extremePortLoadshare2AggControlType": extremePortLoadshare2AggControlType,
       "extremePortRateShapeTable": extremePortRateShapeTable,
       "extremePortRateShapeEntry": extremePortRateShapeEntry,
       "extremePortRateShapePortType": extremePortRateShapePortType,
       "extremePortRateShapeLoopbackTag": extremePortRateShapeLoopbackTag,
       "extremePortRateShapeStatus": extremePortRateShapeStatus,
       "extremePortUtilizationTable": extremePortUtilizationTable,
       "extremePortUtilizationEntry": extremePortUtilizationEntry,
       "extremePortUtilizationAvgTxBw": extremePortUtilizationAvgTxBw,
       "extremePortUtilizationAvgRxBw": extremePortUtilizationAvgRxBw,
       "extremePortUtilizationPeakTxBw": extremePortUtilizationPeakTxBw,
       "extremePortUtilizationPeakRxBw": extremePortUtilizationPeakRxBw,
       "extremePortInfoTable": extremePortInfoTable,
       "extremePortInfoEntry": extremePortInfoEntry,
       "extremePortInfoFilterUpCounter": extremePortInfoFilterUpCounter,
       "extremePortInfoFilterDownCounter": extremePortInfoFilterDownCounter,
       "extremePortXenpakVendorTable": extremePortXenpakVendorTable,
       "extremePortXenpakVendorEntry": extremePortXenpakVendorEntry,
       "extremePortXenpakVendorName": extremePortXenpakVendorName,
       "extremePortIngressStats": extremePortIngressStats,
       "extremePortIngressStatsPortTable": extremePortIngressStatsPortTable,
       "extremePortIngressPortStatsEntry": extremePortIngressPortStatsEntry,
       "extremePortIngressStatsLinkStatus": extremePortIngressStatsLinkStatus,
       "extremePortIngressStatsPortHighPriBytes": extremePortIngressStatsPortHighPriBytes,
       "extremePortIngressStatsPortLowPriBytes": extremePortIngressStatsPortLowPriBytes,
       "extremePortIngressStatsPortDroppedBytes": extremePortIngressStatsPortDroppedBytes,
       "extremePortIngressStatsTxXoff": extremePortIngressStatsTxXoff,
       "extremePortIngressStatsQueueTable": extremePortIngressStatsQueueTable,
       "extremePortIngressQueueStatsEntry": extremePortIngressQueueStatsEntry,
       "extremePortIngressStatsQueueIndex": extremePortIngressStatsQueueIndex,
       "extremePortIngressStatsQueueHighPriBytes": extremePortIngressStatsQueueHighPriBytes,
       "extremePortIngressStatsQueueLowPriBytes": extremePortIngressStatsQueueLowPriBytes,
       "extremePortIngressStatsQueuePercentDropped": extremePortIngressStatsQueuePercentDropped,
       "extremePortEgressRateLimitTable": extremePortEgressRateLimitTable,
       "extremePortEgressRateLimitEntry": extremePortEgressRateLimitEntry,
       "extremePortEgressRateLimitType": extremePortEgressRateLimitType,
       "extremePortEgressRateLimitValue": extremePortEgressRateLimitValue,
       "extremeWiredClientTable": extremeWiredClientTable,
       "extremeWiredClientEntry": extremeWiredClientEntry,
       "extremeWiredClientID": extremeWiredClientID,
       "extremeWiredClientState": extremeWiredClientState,
       "extremeWiredClientVLAN": extremeWiredClientVLAN,
       "extremeWiredClientPriority": extremeWiredClientPriority,
       "extremeWiredClientAuthType": extremeWiredClientAuthType,
       "extremeWiredClientLastStateChangeTime": extremeWiredClientLastStateChangeTime,
       "extremeWiredClientIP": extremeWiredClientIP,
       "extremePortUtilizationExtnTable": extremePortUtilizationExtnTable,
       "extremePortUtilizationExtnEntry": extremePortUtilizationExtnEntry,
       "extremePortUtilizationAvgTxPkts": extremePortUtilizationAvgTxPkts,
       "extremePortUtilizationAvgRxPkts": extremePortUtilizationAvgRxPkts,
       "extremePortUtilizationPeakTxPkts": extremePortUtilizationPeakTxPkts,
       "extremePortUtilizationPeakRxPkts": extremePortUtilizationPeakRxPkts,
       "extremePortUtilizationAvgTxBytes": extremePortUtilizationAvgTxBytes,
       "extremePortUtilizationAvgRxBytes": extremePortUtilizationAvgRxBytes,
       "extremePortUtilizationPeakTxBytes": extremePortUtilizationPeakTxBytes,
       "extremePortUtilizationPeakRxBytes": extremePortUtilizationPeakRxBytes,
       "extremePortQosStatsTable": extremePortQosStatsTable,
       "extremePortQosStatsEntry": extremePortQosStatsEntry,
       "extremePortQosIngress": extremePortQosIngress,
       "extremePortQP0TxBytes": extremePortQP0TxBytes,
       "extremePortQP0TxPkts": extremePortQP0TxPkts,
       "extremePortQP1TxBytes": extremePortQP1TxBytes,
       "extremePortQP1TxPkts": extremePortQP1TxPkts,
       "extremePortQP2TxBytes": extremePortQP2TxBytes,
       "extremePortQP2TxPkts": extremePortQP2TxPkts,
       "extremePortQP3TxBytes": extremePortQP3TxBytes,
       "extremePortQP3TxPkts": extremePortQP3TxPkts,
       "extremePortQP4TxBytes": extremePortQP4TxBytes,
       "extremePortQP4TxPkts": extremePortQP4TxPkts,
       "extremePortQP5TxBytes": extremePortQP5TxBytes,
       "extremePortQP5TxPkts": extremePortQP5TxPkts,
       "extremePortQP6TxBytes": extremePortQP6TxBytes,
       "extremePortQP6TxPkts": extremePortQP6TxPkts,
       "extremePortQP7TxBytes": extremePortQP7TxBytes,
       "extremePortQP7TxPkts": extremePortQP7TxPkts,
       "extremePortMau": extremePortMau,
       "extremePortMauTable": extremePortMauTable,
       "extremePortMauEntry": extremePortMauEntry,
       "extremePortMauType": extremePortMauType,
       "extremePortMauVendorName": extremePortMauVendorName,
       "extremePortMauStatus": extremePortMauStatus,
       "extremePortMauRestrict": extremePortMauRestrict,
       "extremePortMauTraps": extremePortMauTraps,
       "extremePortMauTrapsPrefix": extremePortMauTrapsPrefix,
       "extremePortMauChangeTrap": extremePortMauChangeTrap,
       "extremePortMauRestrictionTrap": extremePortMauRestrictionTrap,
       "extremePortCongestionStatsTable": extremePortCongestionStatsTable,
       "extremePortCongestionStatsEntry": extremePortCongestionStatsEntry,
       "extremePortCongDropPkts": extremePortCongDropPkts,
       "extremePortQosCongestionStatsTable": extremePortQosCongestionStatsTable,
       "extremePortQosCongestionStatsEntry": extremePortQosCongestionStatsEntry,
       "extremePortQP0CongPkts": extremePortQP0CongPkts,
       "extremePortQP1CongPkts": extremePortQP1CongPkts,
       "extremePortQP2CongPkts": extremePortQP2CongPkts,
       "extremePortQP3CongPkts": extremePortQP3CongPkts,
       "extremePortQP4CongPkts": extremePortQP4CongPkts,
       "extremePortQP5CongPkts": extremePortQP5CongPkts,
       "extremePortQP6CongPkts": extremePortQP6CongPkts,
       "extremePortQP7CongPkts": extremePortQP7CongPkts,
       "extremeRateLimitExceededAlarm": extremeRateLimitExceededAlarm,
       "extremePortVlanInfoTable": extremePortVlanInfoTable,
       "extremePortVlanInfoEntry": extremePortVlanInfoEntry,
       "extremePortVlanInfoDescr": extremePortVlanInfoDescr,
       "extremePortVlanInfoLimitLearningEnabled": extremePortVlanInfoLimitLearningEnabled,
       "extremePortVlanInfoLimitLearningNumber": extremePortVlanInfoLimitLearningNumber,
       "extremePortVlanInfoMacLockDownEnabled": extremePortVlanInfoMacLockDownEnabled,
       "extremePortConfigTable": extremePortConfigTable,
       "extremePortConfigEntry": extremePortConfigEntry,
       "extremePortAutoNegotiation": extremePortAutoNegotiation,
       "extremePortAdminSpeed": extremePortAdminSpeed,
       "extremePortDuplex": extremePortDuplex,
       "extremePortMedium": extremePortMedium}
)
