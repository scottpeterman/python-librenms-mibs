# SNMP MIB module (BTI8xx-SFP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bti\BTI8xx-SFP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:22:39 2025
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

(mainSystem,) = mibBuilder.importSymbols(
    "BTI8xx-TC-MIB",
    "mainSystem")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

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

sfp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6)
)
if mibBuilder.loadTexts:
    sfp.setRevisions(
        ("2015-11-20 12:00",
         "2013-12-27 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SfpInfoTable_Object = MibTable
sfpInfoTable = _SfpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    sfpInfoTable.setStatus("current")
_SfpInfoEntry_Object = MibTableRow
sfpInfoEntry = _SfpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1, 1)
)
sfpInfoEntry.setIndexNames(
    (0, "BTI8xx-SFP-MIB", "sfpInfoIndex"),
)
if mibBuilder.loadTexts:
    sfpInfoEntry.setStatus("current")


class _SfpInfoIndex_Type(Integer32):
    """Custom type sfpInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_SfpInfoIndex_Type.__name__ = "Integer32"
_SfpInfoIndex_Object = MibTableColumn
sfpInfoIndex = _SfpInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1, 1, 1),
    _SfpInfoIndex_Type()
)
sfpInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoIndex.setStatus("current")


class _SfpInfoLocation_Type(OctetString):
    """Custom type sfpInfoLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SfpInfoLocation_Type.__name__ = "OctetString"
_SfpInfoLocation_Object = MibTableColumn
sfpInfoLocation = _SfpInfoLocation_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1, 1, 2),
    _SfpInfoLocation_Type()
)
sfpInfoLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoLocation.setStatus("current")


class _SfpInfoSerialNumber_Type(OctetString):
    """Custom type sfpInfoSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SfpInfoSerialNumber_Type.__name__ = "OctetString"
_SfpInfoSerialNumber_Object = MibTableColumn
sfpInfoSerialNumber = _SfpInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1, 1, 3),
    _SfpInfoSerialNumber_Type()
)
sfpInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoSerialNumber.setStatus("current")


class _SfpInfoProductCode_Type(OctetString):
    """Custom type sfpInfoProductCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SfpInfoProductCode_Type.__name__ = "OctetString"
_SfpInfoProductCode_Object = MibTableColumn
sfpInfoProductCode = _SfpInfoProductCode_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1, 1, 4),
    _SfpInfoProductCode_Type()
)
sfpInfoProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoProductCode.setStatus("current")


class _SfpInfoWigth_Type(Integer32):
    """Custom type sfpInfoWigth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SfpInfoWigth_Type.__name__ = "Integer32"
_SfpInfoWigth_Object = MibTableColumn
sfpInfoWigth = _SfpInfoWigth_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1, 1, 5),
    _SfpInfoWigth_Type()
)
sfpInfoWigth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoWigth.setStatus("current")
_SfpInfoDistanceFiber1_Type = DisplayString
_SfpInfoDistanceFiber1_Object = MibTableColumn
sfpInfoDistanceFiber1 = _SfpInfoDistanceFiber1_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1, 1, 6),
    _SfpInfoDistanceFiber1_Type()
)
sfpInfoDistanceFiber1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoDistanceFiber1.setStatus("current")
_SfpInfoDistanceFiber2_Type = DisplayString
_SfpInfoDistanceFiber2_Object = MibTableColumn
sfpInfoDistanceFiber2 = _SfpInfoDistanceFiber2_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1, 1, 7),
    _SfpInfoDistanceFiber2_Type()
)
sfpInfoDistanceFiber2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoDistanceFiber2.setStatus("current")
_SfpInfoDistanceCopper_Type = DisplayString
_SfpInfoDistanceCopper_Object = MibTableColumn
sfpInfoDistanceCopper = _SfpInfoDistanceCopper_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1, 1, 8),
    _SfpInfoDistanceCopper_Type()
)
sfpInfoDistanceCopper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoDistanceCopper.setStatus("current")
_SfpInventoryTable_Object = MibTable
sfpInventoryTable = _SfpInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    sfpInventoryTable.setStatus("current")
_SfpInventoryEntry_Object = MibTableRow
sfpInventoryEntry = _SfpInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 2, 1)
)
sfpInventoryEntry.setIndexNames(
    (0, "BTI8xx-SFP-MIB", "sfpInventoryIndex"),
)
if mibBuilder.loadTexts:
    sfpInventoryEntry.setStatus("current")


class _SfpInventoryIndex_Type(Integer32):
    """Custom type sfpInventoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_SfpInventoryIndex_Type.__name__ = "Integer32"
_SfpInventoryIndex_Object = MibTableColumn
sfpInventoryIndex = _SfpInventoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 2, 1, 1),
    _SfpInventoryIndex_Type()
)
sfpInventoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInventoryIndex.setStatus("current")


class _SfpInventoryLocation_Type(OctetString):
    """Custom type sfpInventoryLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SfpInventoryLocation_Type.__name__ = "OctetString"
_SfpInventoryLocation_Object = MibTableColumn
sfpInventoryLocation = _SfpInventoryLocation_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 2, 1, 2),
    _SfpInventoryLocation_Type()
)
sfpInventoryLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInventoryLocation.setStatus("current")


class _SfpInventoryType_Type(OctetString):
    """Custom type sfpInventoryType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SfpInventoryType_Type.__name__ = "OctetString"
_SfpInventoryType_Object = MibTableColumn
sfpInventoryType = _SfpInventoryType_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 2, 1, 3),
    _SfpInventoryType_Type()
)
sfpInventoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInventoryType.setStatus("current")


class _SfpInventoryPecCode_Type(OctetString):
    """Custom type sfpInventoryPecCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SfpInventoryPecCode_Type.__name__ = "OctetString"
_SfpInventoryPecCode_Object = MibTableColumn
sfpInventoryPecCode = _SfpInventoryPecCode_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 2, 1, 4),
    _SfpInventoryPecCode_Type()
)
sfpInventoryPecCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInventoryPecCode.setStatus("current")


class _SfpInventoryCLEI_Type(OctetString):
    """Custom type sfpInventoryCLEI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SfpInventoryCLEI_Type.__name__ = "OctetString"
_SfpInventoryCLEI_Object = MibTableColumn
sfpInventoryCLEI = _SfpInventoryCLEI_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 2, 1, 5),
    _SfpInventoryCLEI_Type()
)
sfpInventoryCLEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInventoryCLEI.setStatus("current")


class _SfpInventoryStatus_Type(Integer32):
    """Custom type sfpInventoryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("notSupported", 2))
    )


_SfpInventoryStatus_Type.__name__ = "Integer32"
_SfpInventoryStatus_Object = MibTableColumn
sfpInventoryStatus = _SfpInventoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 2, 1, 6),
    _SfpInventoryStatus_Type()
)
sfpInventoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInventoryStatus.setStatus("current")


class _SfpInventoryEqStatus_Type(Integer32):
    """Custom type sfpInventoryEqStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("equipped", 1),
          ("unEquipped", 2))
    )


_SfpInventoryEqStatus_Type.__name__ = "Integer32"
_SfpInventoryEqStatus_Object = MibTableColumn
sfpInventoryEqStatus = _SfpInventoryEqStatus_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 2, 1, 7),
    _SfpInventoryEqStatus_Type()
)
sfpInventoryEqStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInventoryEqStatus.setStatus("current")
_SfpDiagnosticTable_Object = MibTable
sfpDiagnosticTable = _SfpDiagnosticTable_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3)
)
if mibBuilder.loadTexts:
    sfpDiagnosticTable.setStatus("current")
_SfpDiagnosticEntry_Object = MibTableRow
sfpDiagnosticEntry = _SfpDiagnosticEntry_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3, 1)
)
sfpDiagnosticEntry.setIndexNames(
    (0, "BTI8xx-SFP-MIB", "sfpDiagnosticIndex"),
)
if mibBuilder.loadTexts:
    sfpDiagnosticEntry.setStatus("current")


class _SfpDiagnosticIndex_Type(Integer32):
    """Custom type sfpDiagnosticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_SfpDiagnosticIndex_Type.__name__ = "Integer32"
_SfpDiagnosticIndex_Object = MibTableColumn
sfpDiagnosticIndex = _SfpDiagnosticIndex_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3, 1, 1),
    _SfpDiagnosticIndex_Type()
)
sfpDiagnosticIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticIndex.setStatus("current")


class _SfpDiagnosticLocation_Type(OctetString):
    """Custom type sfpDiagnosticLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SfpDiagnosticLocation_Type.__name__ = "OctetString"
_SfpDiagnosticLocation_Object = MibTableColumn
sfpDiagnosticLocation = _SfpDiagnosticLocation_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3, 1, 2),
    _SfpDiagnosticLocation_Type()
)
sfpDiagnosticLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticLocation.setStatus("current")


class _SfpDiagnosticCalibration_Type(OctetString):
    """Custom type sfpDiagnosticCalibration based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SfpDiagnosticCalibration_Type.__name__ = "OctetString"
_SfpDiagnosticCalibration_Object = MibTableColumn
sfpDiagnosticCalibration = _SfpDiagnosticCalibration_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3, 1, 3),
    _SfpDiagnosticCalibration_Type()
)
sfpDiagnosticCalibration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticCalibration.setStatus("current")


class _SfpDiagnosticTemperature_Type(OctetString):
    """Custom type sfpDiagnosticTemperature based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_SfpDiagnosticTemperature_Type.__name__ = "OctetString"
_SfpDiagnosticTemperature_Object = MibTableColumn
sfpDiagnosticTemperature = _SfpDiagnosticTemperature_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3, 1, 4),
    _SfpDiagnosticTemperature_Type()
)
sfpDiagnosticTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticTemperature.setStatus("current")


class _SfpDiagnosticVoltageV_Type(OctetString):
    """Custom type sfpDiagnosticVoltageV based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_SfpDiagnosticVoltageV_Type.__name__ = "OctetString"
_SfpDiagnosticVoltageV_Object = MibTableColumn
sfpDiagnosticVoltageV = _SfpDiagnosticVoltageV_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3, 1, 5),
    _SfpDiagnosticVoltageV_Type()
)
sfpDiagnosticVoltageV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticVoltageV.setStatus("current")


class _SfpDiagnosticTxBiasMA_Type(OctetString):
    """Custom type sfpDiagnosticTxBiasMA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_SfpDiagnosticTxBiasMA_Type.__name__ = "OctetString"
_SfpDiagnosticTxBiasMA_Object = MibTableColumn
sfpDiagnosticTxBiasMA = _SfpDiagnosticTxBiasMA_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3, 1, 6),
    _SfpDiagnosticTxBiasMA_Type()
)
sfpDiagnosticTxBiasMA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticTxBiasMA.setStatus("current")


class _SfpDiagnosticTxPowerDbm_Type(OctetString):
    """Custom type sfpDiagnosticTxPowerDbm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_SfpDiagnosticTxPowerDbm_Type.__name__ = "OctetString"
_SfpDiagnosticTxPowerDbm_Object = MibTableColumn
sfpDiagnosticTxPowerDbm = _SfpDiagnosticTxPowerDbm_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3, 1, 7),
    _SfpDiagnosticTxPowerDbm_Type()
)
sfpDiagnosticTxPowerDbm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticTxPowerDbm.setStatus("current")


class _SfpDiagnosticRxPowerDbm_Type(OctetString):
    """Custom type sfpDiagnosticRxPowerDbm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_SfpDiagnosticRxPowerDbm_Type.__name__ = "OctetString"
_SfpDiagnosticRxPowerDbm_Object = MibTableColumn
sfpDiagnosticRxPowerDbm = _SfpDiagnosticRxPowerDbm_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3, 1, 8),
    _SfpDiagnosticRxPowerDbm_Type()
)
sfpDiagnosticRxPowerDbm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticRxPowerDbm.setStatus("current")
_SfpStatusTable_Object = MibTable
sfpStatusTable = _SfpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 4)
)
if mibBuilder.loadTexts:
    sfpStatusTable.setStatus("current")
_SfpStatusEntry_Object = MibTableRow
sfpStatusEntry = _SfpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 4, 1)
)
sfpStatusEntry.setIndexNames(
    (0, "BTI8xx-SFP-MIB", "sfpStatusIndex"),
)
if mibBuilder.loadTexts:
    sfpStatusEntry.setStatus("current")


class _SfpStatusIndex_Type(Integer32):
    """Custom type sfpStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_SfpStatusIndex_Type.__name__ = "Integer32"
_SfpStatusIndex_Object = MibTableColumn
sfpStatusIndex = _SfpStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 4, 1, 1),
    _SfpStatusIndex_Type()
)
sfpStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpStatusIndex.setStatus("current")


class _SfpStatusLocation_Type(OctetString):
    """Custom type sfpStatusLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SfpStatusLocation_Type.__name__ = "OctetString"
_SfpStatusLocation_Object = MibTableColumn
sfpStatusLocation = _SfpStatusLocation_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 4, 1, 2),
    _SfpStatusLocation_Type()
)
sfpStatusLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpStatusLocation.setStatus("current")


class _SfpStatusEqStatus_Type(Integer32):
    """Custom type sfpStatusEqStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("equipped", 1),
          ("unEquipped", 2))
    )


_SfpStatusEqStatus_Type.__name__ = "Integer32"
_SfpStatusEqStatus_Object = MibTableColumn
sfpStatusEqStatus = _SfpStatusEqStatus_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 4, 1, 3),
    _SfpStatusEqStatus_Type()
)
sfpStatusEqStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpStatusEqStatus.setStatus("current")


class _SfpStatusRxStatus_Type(OctetString):
    """Custom type sfpStatusRxStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SfpStatusRxStatus_Type.__name__ = "OctetString"
_SfpStatusRxStatus_Object = MibTableColumn
sfpStatusRxStatus = _SfpStatusRxStatus_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 4, 1, 4),
    _SfpStatusRxStatus_Type()
)
sfpStatusRxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpStatusRxStatus.setStatus("current")


class _SfpStatusTxStatus_Type(OctetString):
    """Custom type sfpStatusTxStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SfpStatusTxStatus_Type.__name__ = "OctetString"
_SfpStatusTxStatus_Object = MibTableColumn
sfpStatusTxStatus = _SfpStatusTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 4, 1, 5),
    _SfpStatusTxStatus_Type()
)
sfpStatusTxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpStatusTxStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BTI8xx-SFP-MIB",
    **{"sfp": sfp,
       "sfpInfoTable": sfpInfoTable,
       "sfpInfoEntry": sfpInfoEntry,
       "sfpInfoIndex": sfpInfoIndex,
       "sfpInfoLocation": sfpInfoLocation,
       "sfpInfoSerialNumber": sfpInfoSerialNumber,
       "sfpInfoProductCode": sfpInfoProductCode,
       "sfpInfoWigth": sfpInfoWigth,
       "sfpInfoDistanceFiber1": sfpInfoDistanceFiber1,
       "sfpInfoDistanceFiber2": sfpInfoDistanceFiber2,
       "sfpInfoDistanceCopper": sfpInfoDistanceCopper,
       "sfpInventoryTable": sfpInventoryTable,
       "sfpInventoryEntry": sfpInventoryEntry,
       "sfpInventoryIndex": sfpInventoryIndex,
       "sfpInventoryLocation": sfpInventoryLocation,
       "sfpInventoryType": sfpInventoryType,
       "sfpInventoryPecCode": sfpInventoryPecCode,
       "sfpInventoryCLEI": sfpInventoryCLEI,
       "sfpInventoryStatus": sfpInventoryStatus,
       "sfpInventoryEqStatus": sfpInventoryEqStatus,
       "sfpDiagnosticTable": sfpDiagnosticTable,
       "sfpDiagnosticEntry": sfpDiagnosticEntry,
       "sfpDiagnosticIndex": sfpDiagnosticIndex,
       "sfpDiagnosticLocation": sfpDiagnosticLocation,
       "sfpDiagnosticCalibration": sfpDiagnosticCalibration,
       "sfpDiagnosticTemperature": sfpDiagnosticTemperature,
       "sfpDiagnosticVoltageV": sfpDiagnosticVoltageV,
       "sfpDiagnosticTxBiasMA": sfpDiagnosticTxBiasMA,
       "sfpDiagnosticTxPowerDbm": sfpDiagnosticTxPowerDbm,
       "sfpDiagnosticRxPowerDbm": sfpDiagnosticRxPowerDbm,
       "sfpStatusTable": sfpStatusTable,
       "sfpStatusEntry": sfpStatusEntry,
       "sfpStatusIndex": sfpStatusIndex,
       "sfpStatusLocation": sfpStatusLocation,
       "sfpStatusEqStatus": sfpStatusEqStatus,
       "sfpStatusRxStatus": sfpStatusRxStatus,
       "sfpStatusTxStatus": sfpStatusTxStatus}
)
