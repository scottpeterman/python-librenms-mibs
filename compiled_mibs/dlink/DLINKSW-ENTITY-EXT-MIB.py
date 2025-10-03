# SNMP MIB module (DLINKSW-ENTITY-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-ENTITY-EXT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:03 2025
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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

dlinkSwEntityExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 5)
)
if mibBuilder.loadTexts:
    dlinkSwEntityExtMIB.setRevisions(
        ("2013-09-06 00:00",
         "2013-03-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DEntityExtNotifications_ObjectIdentity = ObjectIdentity
dEntityExtNotifications = _DEntityExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 0)
)
_DEntityExtObjects_ObjectIdentity = ObjectIdentity
dEntityExtObjects = _DEntityExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1)
)
_DEntityExtEnvObjects_ObjectIdentity = ObjectIdentity
dEntityExtEnvObjects = _DEntityExtEnvObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 1)
)
_DEntityExtEnvTempTable_Object = MibTable
dEntityExtEnvTempTable = _DEntityExtEnvTempTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dEntityExtEnvTempTable.setStatus("current")
_DEntityExtEnvTempEntry_Object = MibTableRow
dEntityExtEnvTempEntry = _DEntityExtEnvTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 1, 1, 1)
)
dEntityExtEnvTempEntry.setIndexNames(
    (0, "DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvTempUnitId"),
    (0, "DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvTempIndex"),
)
if mibBuilder.loadTexts:
    dEntityExtEnvTempEntry.setStatus("current")


class _DEntityExtEnvTempUnitId_Type(Unsigned32):
    """Custom type dEntityExtEnvTempUnitId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DEntityExtEnvTempUnitId_Type.__name__ = "Unsigned32"
_DEntityExtEnvTempUnitId_Object = MibTableColumn
dEntityExtEnvTempUnitId = _DEntityExtEnvTempUnitId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 1, 1, 1, 1),
    _DEntityExtEnvTempUnitId_Type()
)
dEntityExtEnvTempUnitId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dEntityExtEnvTempUnitId.setStatus("current")


class _DEntityExtEnvTempIndex_Type(Integer32):
    """Custom type dEntityExtEnvTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DEntityExtEnvTempIndex_Type.__name__ = "Integer32"
_DEntityExtEnvTempIndex_Object = MibTableColumn
dEntityExtEnvTempIndex = _DEntityExtEnvTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 1, 1, 1, 2),
    _DEntityExtEnvTempIndex_Type()
)
dEntityExtEnvTempIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dEntityExtEnvTempIndex.setStatus("current")


class _DEntityExtEnvTempDescr_Type(DisplayString):
    """Custom type dEntityExtEnvTempDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DEntityExtEnvTempDescr_Type.__name__ = "DisplayString"
_DEntityExtEnvTempDescr_Object = MibTableColumn
dEntityExtEnvTempDescr = _DEntityExtEnvTempDescr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 1, 1, 1, 3),
    _DEntityExtEnvTempDescr_Type()
)
dEntityExtEnvTempDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dEntityExtEnvTempDescr.setStatus("current")
_DEntityExtEnvTempCurrent_Type = Integer32
_DEntityExtEnvTempCurrent_Object = MibTableColumn
dEntityExtEnvTempCurrent = _DEntityExtEnvTempCurrent_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 1, 1, 1, 4),
    _DEntityExtEnvTempCurrent_Type()
)
dEntityExtEnvTempCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dEntityExtEnvTempCurrent.setStatus("current")
if mibBuilder.loadTexts:
    dEntityExtEnvTempCurrent.setUnits("degrees Celsius")
_DEntityExtEnvTempThresholdLow_Type = Integer32
_DEntityExtEnvTempThresholdLow_Object = MibTableColumn
dEntityExtEnvTempThresholdLow = _DEntityExtEnvTempThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 1, 1, 1, 5),
    _DEntityExtEnvTempThresholdLow_Type()
)
dEntityExtEnvTempThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dEntityExtEnvTempThresholdLow.setStatus("current")
if mibBuilder.loadTexts:
    dEntityExtEnvTempThresholdLow.setUnits("degrees Celsius")
_DEntityExtEnvTempThresholdHigh_Type = Integer32
_DEntityExtEnvTempThresholdHigh_Object = MibTableColumn
dEntityExtEnvTempThresholdHigh = _DEntityExtEnvTempThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 1, 1, 1, 6),
    _DEntityExtEnvTempThresholdHigh_Type()
)
dEntityExtEnvTempThresholdHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dEntityExtEnvTempThresholdHigh.setStatus("current")
if mibBuilder.loadTexts:
    dEntityExtEnvTempThresholdHigh.setUnits("degrees Celsius")


class _DEntityExtEnvTempStatus_Type(Integer32):
    """Custom type dEntityExtEnvTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("abnormal", 2))
    )


_DEntityExtEnvTempStatus_Type.__name__ = "Integer32"
_DEntityExtEnvTempStatus_Object = MibTableColumn
dEntityExtEnvTempStatus = _DEntityExtEnvTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 1, 1, 1, 7),
    _DEntityExtEnvTempStatus_Type()
)
dEntityExtEnvTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dEntityExtEnvTempStatus.setStatus("current")
_DEntityExtEnvFanTable_Object = MibTable
dEntityExtEnvFanTable = _DEntityExtEnvFanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dEntityExtEnvFanTable.setStatus("current")
_DEntityExtEnvFanEntry_Object = MibTableRow
dEntityExtEnvFanEntry = _DEntityExtEnvFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 1, 2, 1)
)
dEntityExtEnvFanEntry.setIndexNames(
    (0, "DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvFanUnitId"),
    (0, "DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvFanIndex"),
)
if mibBuilder.loadTexts:
    dEntityExtEnvFanEntry.setStatus("current")


class _DEntityExtEnvFanUnitId_Type(Unsigned32):
    """Custom type dEntityExtEnvFanUnitId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DEntityExtEnvFanUnitId_Type.__name__ = "Unsigned32"
_DEntityExtEnvFanUnitId_Object = MibTableColumn
dEntityExtEnvFanUnitId = _DEntityExtEnvFanUnitId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 1, 2, 1, 1),
    _DEntityExtEnvFanUnitId_Type()
)
dEntityExtEnvFanUnitId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dEntityExtEnvFanUnitId.setStatus("current")


class _DEntityExtEnvFanIndex_Type(Integer32):
    """Custom type dEntityExtEnvFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DEntityExtEnvFanIndex_Type.__name__ = "Integer32"
_DEntityExtEnvFanIndex_Object = MibTableColumn
dEntityExtEnvFanIndex = _DEntityExtEnvFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 1, 2, 1, 2),
    _DEntityExtEnvFanIndex_Type()
)
dEntityExtEnvFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dEntityExtEnvFanIndex.setStatus("current")


class _DEntityExtEnvFanDescr_Type(DisplayString):
    """Custom type dEntityExtEnvFanDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DEntityExtEnvFanDescr_Type.__name__ = "DisplayString"
_DEntityExtEnvFanDescr_Object = MibTableColumn
dEntityExtEnvFanDescr = _DEntityExtEnvFanDescr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 1, 2, 1, 3),
    _DEntityExtEnvFanDescr_Type()
)
dEntityExtEnvFanDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dEntityExtEnvFanDescr.setStatus("current")


class _DEntityExtEnvFanStatus_Type(Integer32):
    """Custom type dEntityExtEnvFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("fault", 2))
    )


_DEntityExtEnvFanStatus_Type.__name__ = "Integer32"
_DEntityExtEnvFanStatus_Object = MibTableColumn
dEntityExtEnvFanStatus = _DEntityExtEnvFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 1, 2, 1, 4),
    _DEntityExtEnvFanStatus_Type()
)
dEntityExtEnvFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dEntityExtEnvFanStatus.setStatus("current")
_DEntityExtEnvPowerTable_Object = MibTable
dEntityExtEnvPowerTable = _DEntityExtEnvPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 1, 3)
)
if mibBuilder.loadTexts:
    dEntityExtEnvPowerTable.setStatus("current")
_DEntityExtEnvPowerEntry_Object = MibTableRow
dEntityExtEnvPowerEntry = _DEntityExtEnvPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 1, 3, 1)
)
dEntityExtEnvPowerEntry.setIndexNames(
    (0, "DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvPowerUnitId"),
    (0, "DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvPowerIndex"),
)
if mibBuilder.loadTexts:
    dEntityExtEnvPowerEntry.setStatus("current")


class _DEntityExtEnvPowerUnitId_Type(Unsigned32):
    """Custom type dEntityExtEnvPowerUnitId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DEntityExtEnvPowerUnitId_Type.__name__ = "Unsigned32"
_DEntityExtEnvPowerUnitId_Object = MibTableColumn
dEntityExtEnvPowerUnitId = _DEntityExtEnvPowerUnitId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 1, 3, 1, 1),
    _DEntityExtEnvPowerUnitId_Type()
)
dEntityExtEnvPowerUnitId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dEntityExtEnvPowerUnitId.setStatus("current")


class _DEntityExtEnvPowerIndex_Type(Unsigned32):
    """Custom type dEntityExtEnvPowerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DEntityExtEnvPowerIndex_Type.__name__ = "Unsigned32"
_DEntityExtEnvPowerIndex_Object = MibTableColumn
dEntityExtEnvPowerIndex = _DEntityExtEnvPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 1, 3, 1, 2),
    _DEntityExtEnvPowerIndex_Type()
)
dEntityExtEnvPowerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dEntityExtEnvPowerIndex.setStatus("current")


class _DEntityExtEnvPowerDescr_Type(DisplayString):
    """Custom type dEntityExtEnvPowerDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DEntityExtEnvPowerDescr_Type.__name__ = "DisplayString"
_DEntityExtEnvPowerDescr_Object = MibTableColumn
dEntityExtEnvPowerDescr = _DEntityExtEnvPowerDescr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 1, 3, 1, 3),
    _DEntityExtEnvPowerDescr_Type()
)
dEntityExtEnvPowerDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dEntityExtEnvPowerDescr.setStatus("current")
_DEntityExtEnvPowerUsedPower_Type = Unsigned32
_DEntityExtEnvPowerUsedPower_Object = MibTableColumn
dEntityExtEnvPowerUsedPower = _DEntityExtEnvPowerUsedPower_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 1, 3, 1, 4),
    _DEntityExtEnvPowerUsedPower_Type()
)
dEntityExtEnvPowerUsedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dEntityExtEnvPowerUsedPower.setStatus("current")
if mibBuilder.loadTexts:
    dEntityExtEnvPowerUsedPower.setUnits("watts")
_DEntityExtEnvPowerMaxPower_Type = Unsigned32
_DEntityExtEnvPowerMaxPower_Object = MibTableColumn
dEntityExtEnvPowerMaxPower = _DEntityExtEnvPowerMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 1, 3, 1, 5),
    _DEntityExtEnvPowerMaxPower_Type()
)
dEntityExtEnvPowerMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dEntityExtEnvPowerMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    dEntityExtEnvPowerMaxPower.setUnits("watts")


class _DEntityExtEnvPowerStatus_Type(Integer32):
    """Custom type dEntityExtEnvPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inOperation", 1),
          ("failed", 2),
          ("empty", 3))
    )


_DEntityExtEnvPowerStatus_Type.__name__ = "Integer32"
_DEntityExtEnvPowerStatus_Object = MibTableColumn
dEntityExtEnvPowerStatus = _DEntityExtEnvPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 1, 3, 1, 6),
    _DEntityExtEnvPowerStatus_Type()
)
dEntityExtEnvPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dEntityExtEnvPowerStatus.setStatus("current")
_DEntityExtEnvAirFlowTable_Object = MibTable
dEntityExtEnvAirFlowTable = _DEntityExtEnvAirFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 1, 4)
)
if mibBuilder.loadTexts:
    dEntityExtEnvAirFlowTable.setStatus("current")
_DEntityExtEnvAirFlowEntry_Object = MibTableRow
dEntityExtEnvAirFlowEntry = _DEntityExtEnvAirFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 1, 4, 1)
)
dEntityExtEnvAirFlowEntry.setIndexNames(
    (0, "DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvAirFlowUnitId"),
)
if mibBuilder.loadTexts:
    dEntityExtEnvAirFlowEntry.setStatus("current")


class _DEntityExtEnvAirFlowUnitId_Type(Unsigned32):
    """Custom type dEntityExtEnvAirFlowUnitId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DEntityExtEnvAirFlowUnitId_Type.__name__ = "Unsigned32"
_DEntityExtEnvAirFlowUnitId_Object = MibTableColumn
dEntityExtEnvAirFlowUnitId = _DEntityExtEnvAirFlowUnitId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 1, 4, 1, 1),
    _DEntityExtEnvAirFlowUnitId_Type()
)
dEntityExtEnvAirFlowUnitId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dEntityExtEnvAirFlowUnitId.setStatus("current")


class _DEntityExtEnvAirFlowStatus_Type(Integer32):
    """Custom type dEntityExtEnvAirFlowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("abnormal", 2))
    )


_DEntityExtEnvAirFlowStatus_Type.__name__ = "Integer32"
_DEntityExtEnvAirFlowStatus_Object = MibTableColumn
dEntityExtEnvAirFlowStatus = _DEntityExtEnvAirFlowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 1, 4, 1, 2),
    _DEntityExtEnvAirFlowStatus_Type()
)
dEntityExtEnvAirFlowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dEntityExtEnvAirFlowStatus.setStatus("current")
_DEntityExtEnvTrap_ObjectIdentity = ObjectIdentity
dEntityExtEnvTrap = _DEntityExtEnvTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 2)
)


class _DEntityExtEnvNotifyEnable_Type(Bits):
    """Custom type dEntityExtEnvNotifyEnable based on Bits"""
    namedValues = NamedValues(
        *(("fan", 0),
          ("power", 1),
          ("temperature", 2))
    )

_DEntityExtEnvNotifyEnable_Type.__name__ = "Bits"
_DEntityExtEnvNotifyEnable_Object = MibScalar
dEntityExtEnvNotifyEnable = _DEntityExtEnvNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 2, 1),
    _DEntityExtEnvNotifyEnable_Type()
)
dEntityExtEnvNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dEntityExtEnvNotifyEnable.setStatus("current")
_DEntityExtUnitTable_Object = MibTable
dEntityExtUnitTable = _DEntityExtUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 3)
)
if mibBuilder.loadTexts:
    dEntityExtUnitTable.setStatus("current")
_DEntityExtUnitEntry_Object = MibTableRow
dEntityExtUnitEntry = _DEntityExtUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 3, 1)
)
dEntityExtUnitEntry.setIndexNames(
    (0, "DLINKSW-ENTITY-EXT-MIB", "dEntityExtUnitIndex"),
)
if mibBuilder.loadTexts:
    dEntityExtUnitEntry.setStatus("current")


class _DEntityExtUnitIndex_Type(Unsigned32):
    """Custom type dEntityExtUnitIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DEntityExtUnitIndex_Type.__name__ = "Unsigned32"
_DEntityExtUnitIndex_Object = MibTableColumn
dEntityExtUnitIndex = _DEntityExtUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 3, 1, 1),
    _DEntityExtUnitIndex_Type()
)
dEntityExtUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dEntityExtUnitIndex.setStatus("current")


class _DEntityExtUnitStatus_Type(Integer32):
    """Custom type dEntityExtUnitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("failed", 2),
          ("empty", 3))
    )


_DEntityExtUnitStatus_Type.__name__ = "Integer32"
_DEntityExtUnitStatus_Object = MibTableColumn
dEntityExtUnitStatus = _DEntityExtUnitStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 3, 1, 2),
    _DEntityExtUnitStatus_Type()
)
dEntityExtUnitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dEntityExtUnitStatus.setStatus("current")
_DEntityExtUnitUpTime_Type = Unsigned32
_DEntityExtUnitUpTime_Object = MibTableColumn
dEntityExtUnitUpTime = _DEntityExtUnitUpTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 3, 1, 3),
    _DEntityExtUnitUpTime_Type()
)
dEntityExtUnitUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dEntityExtUnitUpTime.setStatus("current")
if mibBuilder.loadTexts:
    dEntityExtUnitUpTime.setUnits("seconds")
_DEntityExtMemoryUtilTable_Object = MibTable
dEntityExtMemoryUtilTable = _DEntityExtMemoryUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 4)
)
if mibBuilder.loadTexts:
    dEntityExtMemoryUtilTable.setStatus("current")
_DEntityExtMemoryUtilEntry_Object = MibTableRow
dEntityExtMemoryUtilEntry = _DEntityExtMemoryUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 4, 1)
)
dEntityExtMemoryUtilEntry.setIndexNames(
    (0, "DLINKSW-ENTITY-EXT-MIB", "dEntityExtMemUtilUnitId"),
    (0, "DLINKSW-ENTITY-EXT-MIB", "dEntityExtMemUtilType"),
)
if mibBuilder.loadTexts:
    dEntityExtMemoryUtilEntry.setStatus("current")


class _DEntityExtMemUtilUnitId_Type(Integer32):
    """Custom type dEntityExtMemUtilUnitId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DEntityExtMemUtilUnitId_Type.__name__ = "Integer32"
_DEntityExtMemUtilUnitId_Object = MibTableColumn
dEntityExtMemUtilUnitId = _DEntityExtMemUtilUnitId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 4, 1, 1),
    _DEntityExtMemUtilUnitId_Type()
)
dEntityExtMemUtilUnitId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dEntityExtMemUtilUnitId.setStatus("current")


class _DEntityExtMemUtilType_Type(Integer32):
    """Custom type dEntityExtMemUtilType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dram", 1),
          ("flash", 2),
          ("nvram", 3))
    )


_DEntityExtMemUtilType_Type.__name__ = "Integer32"
_DEntityExtMemUtilType_Object = MibTableColumn
dEntityExtMemUtilType = _DEntityExtMemUtilType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 4, 1, 2),
    _DEntityExtMemUtilType_Type()
)
dEntityExtMemUtilType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dEntityExtMemUtilType.setStatus("current")
_DEntityExtMemUtilTotal_Type = Unsigned32
_DEntityExtMemUtilTotal_Object = MibTableColumn
dEntityExtMemUtilTotal = _DEntityExtMemUtilTotal_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 4, 1, 3),
    _DEntityExtMemUtilTotal_Type()
)
dEntityExtMemUtilTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dEntityExtMemUtilTotal.setStatus("current")
if mibBuilder.loadTexts:
    dEntityExtMemUtilTotal.setUnits("KB")
_DEntityExtMemUtilUsed_Type = Unsigned32
_DEntityExtMemUtilUsed_Object = MibTableColumn
dEntityExtMemUtilUsed = _DEntityExtMemUtilUsed_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 4, 1, 4),
    _DEntityExtMemUtilUsed_Type()
)
dEntityExtMemUtilUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dEntityExtMemUtilUsed.setStatus("current")
if mibBuilder.loadTexts:
    dEntityExtMemUtilUsed.setUnits("KB")
_DEntityExtMemUtilFree_Type = Unsigned32
_DEntityExtMemUtilFree_Object = MibTableColumn
dEntityExtMemUtilFree = _DEntityExtMemUtilFree_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 4, 1, 5),
    _DEntityExtMemUtilFree_Type()
)
dEntityExtMemUtilFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dEntityExtMemUtilFree.setStatus("current")
if mibBuilder.loadTexts:
    dEntityExtMemUtilFree.setUnits("KB")
_DEntityExtCpuUtilTable_Object = MibTable
dEntityExtCpuUtilTable = _DEntityExtCpuUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 7)
)
if mibBuilder.loadTexts:
    dEntityExtCpuUtilTable.setStatus("current")
_DEntityExtCpuUtilEntry_Object = MibTableRow
dEntityExtCpuUtilEntry = _DEntityExtCpuUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 7, 1)
)
dEntityExtCpuUtilEntry.setIndexNames(
    (0, "DLINKSW-ENTITY-EXT-MIB", "dEntityExtCpuUtilUnitId"),
    (0, "DLINKSW-ENTITY-EXT-MIB", "dEntityExtCpuUtilCpuID"),
)
if mibBuilder.loadTexts:
    dEntityExtCpuUtilEntry.setStatus("current")


class _DEntityExtCpuUtilUnitId_Type(Unsigned32):
    """Custom type dEntityExtCpuUtilUnitId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DEntityExtCpuUtilUnitId_Type.__name__ = "Unsigned32"
_DEntityExtCpuUtilUnitId_Object = MibTableColumn
dEntityExtCpuUtilUnitId = _DEntityExtCpuUtilUnitId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 7, 1, 1),
    _DEntityExtCpuUtilUnitId_Type()
)
dEntityExtCpuUtilUnitId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dEntityExtCpuUtilUnitId.setStatus("current")


class _DEntityExtCpuUtilCpuID_Type(Unsigned32):
    """Custom type dEntityExtCpuUtilCpuID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DEntityExtCpuUtilCpuID_Type.__name__ = "Unsigned32"
_DEntityExtCpuUtilCpuID_Object = MibTableColumn
dEntityExtCpuUtilCpuID = _DEntityExtCpuUtilCpuID_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 7, 1, 2),
    _DEntityExtCpuUtilCpuID_Type()
)
dEntityExtCpuUtilCpuID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dEntityExtCpuUtilCpuID.setStatus("current")
_DEntityExtCpuUtilFiveSeconds_Type = Unsigned32
_DEntityExtCpuUtilFiveSeconds_Object = MibTableColumn
dEntityExtCpuUtilFiveSeconds = _DEntityExtCpuUtilFiveSeconds_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 7, 1, 3),
    _DEntityExtCpuUtilFiveSeconds_Type()
)
dEntityExtCpuUtilFiveSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dEntityExtCpuUtilFiveSeconds.setStatus("current")
if mibBuilder.loadTexts:
    dEntityExtCpuUtilFiveSeconds.setUnits("percentage")
_DEntityExtCpuUtilOneMinute_Type = Unsigned32
_DEntityExtCpuUtilOneMinute_Object = MibTableColumn
dEntityExtCpuUtilOneMinute = _DEntityExtCpuUtilOneMinute_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 7, 1, 4),
    _DEntityExtCpuUtilOneMinute_Type()
)
dEntityExtCpuUtilOneMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dEntityExtCpuUtilOneMinute.setStatus("current")
if mibBuilder.loadTexts:
    dEntityExtCpuUtilOneMinute.setUnits("percentage")
_DEntityExtCpuUtilFiveMinutes_Type = Unsigned32
_DEntityExtCpuUtilFiveMinutes_Object = MibTableColumn
dEntityExtCpuUtilFiveMinutes = _DEntityExtCpuUtilFiveMinutes_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 7, 1, 5),
    _DEntityExtCpuUtilFiveMinutes_Type()
)
dEntityExtCpuUtilFiveMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dEntityExtCpuUtilFiveMinutes.setStatus("current")
_DEntityExtVersionTable_Object = MibTable
dEntityExtVersionTable = _DEntityExtVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 8)
)
if mibBuilder.loadTexts:
    dEntityExtVersionTable.setStatus("current")
_DEntityExtVersionEntry_Object = MibTableRow
dEntityExtVersionEntry = _DEntityExtVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 8, 1)
)
dEntityExtVersionEntry.setIndexNames(
    (0, "DLINKSW-ENTITY-EXT-MIB", "dEntityExtVersionUnitId"),
)
if mibBuilder.loadTexts:
    dEntityExtVersionEntry.setStatus("current")


class _DEntityExtVersionUnitId_Type(Unsigned32):
    """Custom type dEntityExtVersionUnitId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DEntityExtVersionUnitId_Type.__name__ = "Unsigned32"
_DEntityExtVersionUnitId_Object = MibTableColumn
dEntityExtVersionUnitId = _DEntityExtVersionUnitId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 8, 1, 1),
    _DEntityExtVersionUnitId_Type()
)
dEntityExtVersionUnitId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dEntityExtVersionUnitId.setStatus("current")


class _DEntityExtVersionBootloader_Type(DisplayString):
    """Custom type dEntityExtVersionBootloader based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DEntityExtVersionBootloader_Type.__name__ = "DisplayString"
_DEntityExtVersionBootloader_Object = MibTableColumn
dEntityExtVersionBootloader = _DEntityExtVersionBootloader_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 8, 1, 2),
    _DEntityExtVersionBootloader_Type()
)
dEntityExtVersionBootloader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dEntityExtVersionBootloader.setStatus("current")


class _DEntityExtVersionRuntime_Type(DisplayString):
    """Custom type dEntityExtVersionRuntime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DEntityExtVersionRuntime_Type.__name__ = "DisplayString"
_DEntityExtVersionRuntime_Object = MibTableColumn
dEntityExtVersionRuntime = _DEntityExtVersionRuntime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 1, 8, 1, 3),
    _DEntityExtVersionRuntime_Type()
)
dEntityExtVersionRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dEntityExtVersionRuntime.setStatus("current")
_DEntityExtConformance_ObjectIdentity = ObjectIdentity
dEntityExtConformance = _DEntityExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 2)
)
_DEntityExtMIBCompliances_ObjectIdentity = ObjectIdentity
dEntityExtMIBCompliances = _DEntityExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 2, 1)
)
_DEntityExtMIBGroups_ObjectIdentity = ObjectIdentity
dEntityExtMIBGroups = _DEntityExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 2, 2)
)

# Managed Objects groups

dEntityExtTempGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 2, 2, 1)
)
dEntityExtTempGroup.setObjects(
      *(("DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvTempDescr"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvTempCurrent"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvTempThresholdLow"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvTempThresholdHigh"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvTempStatus"))
)
if mibBuilder.loadTexts:
    dEntityExtTempGroup.setStatus("current")

dEntityExtFanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 2, 2, 2)
)
dEntityExtFanGroup.setObjects(
      *(("DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvFanDescr"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvFanStatus"))
)
if mibBuilder.loadTexts:
    dEntityExtFanGroup.setStatus("current")

dEntityExtPowerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 2, 2, 3)
)
dEntityExtPowerGroup.setObjects(
      *(("DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvPowerDescr"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvPowerUsedPower"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvPowerMaxPower"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvPowerStatus"))
)
if mibBuilder.loadTexts:
    dEntityExtPowerGroup.setStatus("current")

dEntityExtSystemInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 2, 2, 4)
)
dEntityExtSystemInfoGroup.setObjects(
      *(("DLINKSW-ENTITY-EXT-MIB", "dEntityExtUnitStatus"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtUnitUpTime"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtMemUtilTotal"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtMemUtilUsed"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtMemUtilFree"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtCpuUtilFiveSeconds"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtCpuUtilOneMinute"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtCpuUtilFiveMinutes"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtVersionBootloader"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtVersionRuntime"))
)
if mibBuilder.loadTexts:
    dEntityExtSystemInfoGroup.setStatus("current")

dEntityExtGenericNotifInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 2, 2, 5)
)
dEntityExtGenericNotifInfoGroup.setObjects(
    ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvNotifyEnable")
)
if mibBuilder.loadTexts:
    dEntityExtGenericNotifInfoGroup.setStatus("current")


# Notification objects

dEntityExtFanStatusChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 0, 1)
)
dEntityExtFanStatusChg.setObjects(
      *(("DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvFanUnitId"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvFanIndex"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvFanStatus"))
)
if mibBuilder.loadTexts:
    dEntityExtFanStatusChg.setStatus(
        "current"
    )

dEntityExtThermalStatusChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 0, 2)
)
dEntityExtThermalStatusChg.setObjects(
      *(("DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvTempUnitId"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvTempIndex"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvTempStatus"))
)
if mibBuilder.loadTexts:
    dEntityExtThermalStatusChg.setStatus(
        "current"
    )

dEntityExtPowerStatusChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 0, 3)
)
dEntityExtPowerStatusChg.setObjects(
      *(("DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvPowerUnitId"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvPowerIndex"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvPowerStatus"))
)
if mibBuilder.loadTexts:
    dEntityExtPowerStatusChg.setStatus(
        "current"
    )

dEntityExtAirFlowChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 0, 4)
)
dEntityExtAirFlowChg.setObjects(
      *(("DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvAirFlowUnitId"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtEnvAirFlowStatus"))
)
if mibBuilder.loadTexts:
    dEntityExtAirFlowChg.setStatus(
        "current"
    )

dEntityExtFactoryResetButton = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 0, 5)
)
dEntityExtFactoryResetButton.setObjects(
    ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtUnitIndex")
)
if mibBuilder.loadTexts:
    dEntityExtFactoryResetButton.setStatus(
        "current"
    )


# Notifications groups

dEntityExtFanNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 2, 2, 6)
)
dEntityExtFanNotifGroup.setObjects(
    ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtFanStatusChg")
)
if mibBuilder.loadTexts:
    dEntityExtFanNotifGroup.setStatus(
        "current"
    )

dEntityExtThermalNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 2, 2, 7)
)
dEntityExtThermalNotifGroup.setObjects(
    ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtThermalStatusChg")
)
if mibBuilder.loadTexts:
    dEntityExtThermalNotifGroup.setStatus(
        "current"
    )

dEntityExtPowerNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 2, 2, 8)
)
dEntityExtPowerNotifGroup.setObjects(
    ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtPowerStatusChg")
)
if mibBuilder.loadTexts:
    dEntityExtPowerNotifGroup.setStatus(
        "current"
    )

dEntityExtAirFlowNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 2, 2, 9)
)
dEntityExtAirFlowNotifGroup.setObjects(
    ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtAirFlowChg")
)
if mibBuilder.loadTexts:
    dEntityExtAirFlowNotifGroup.setStatus(
        "current"
    )

dEntityExtFactoryResetButtonNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 2, 2, 10)
)
dEntityExtFactoryResetButtonNotifGroup.setObjects(
    ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtFactoryResetButton")
)
if mibBuilder.loadTexts:
    dEntityExtFactoryResetButtonNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dEntityExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 5, 2, 1, 1)
)
dEntityExtCompliance.setObjects(
      *(("DLINKSW-ENTITY-EXT-MIB", "dEntityExtSystemInfoGroup"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtTempGroup"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtThermalNotifGroup"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtFanGroup"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtFanNotifGroup"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtPowerGroup"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtPowerNotifGroup"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtAirFlowNotifGroup"),
        ("DLINKSW-ENTITY-EXT-MIB", "dEntityExtGenericNotifInfoGroup"))
)
if mibBuilder.loadTexts:
    dEntityExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-ENTITY-EXT-MIB",
    **{"dlinkSwEntityExtMIB": dlinkSwEntityExtMIB,
       "dEntityExtNotifications": dEntityExtNotifications,
       "dEntityExtFanStatusChg": dEntityExtFanStatusChg,
       "dEntityExtThermalStatusChg": dEntityExtThermalStatusChg,
       "dEntityExtPowerStatusChg": dEntityExtPowerStatusChg,
       "dEntityExtAirFlowChg": dEntityExtAirFlowChg,
       "dEntityExtFactoryResetButton": dEntityExtFactoryResetButton,
       "dEntityExtObjects": dEntityExtObjects,
       "dEntityExtEnvObjects": dEntityExtEnvObjects,
       "dEntityExtEnvTempTable": dEntityExtEnvTempTable,
       "dEntityExtEnvTempEntry": dEntityExtEnvTempEntry,
       "dEntityExtEnvTempUnitId": dEntityExtEnvTempUnitId,
       "dEntityExtEnvTempIndex": dEntityExtEnvTempIndex,
       "dEntityExtEnvTempDescr": dEntityExtEnvTempDescr,
       "dEntityExtEnvTempCurrent": dEntityExtEnvTempCurrent,
       "dEntityExtEnvTempThresholdLow": dEntityExtEnvTempThresholdLow,
       "dEntityExtEnvTempThresholdHigh": dEntityExtEnvTempThresholdHigh,
       "dEntityExtEnvTempStatus": dEntityExtEnvTempStatus,
       "dEntityExtEnvFanTable": dEntityExtEnvFanTable,
       "dEntityExtEnvFanEntry": dEntityExtEnvFanEntry,
       "dEntityExtEnvFanUnitId": dEntityExtEnvFanUnitId,
       "dEntityExtEnvFanIndex": dEntityExtEnvFanIndex,
       "dEntityExtEnvFanDescr": dEntityExtEnvFanDescr,
       "dEntityExtEnvFanStatus": dEntityExtEnvFanStatus,
       "dEntityExtEnvPowerTable": dEntityExtEnvPowerTable,
       "dEntityExtEnvPowerEntry": dEntityExtEnvPowerEntry,
       "dEntityExtEnvPowerUnitId": dEntityExtEnvPowerUnitId,
       "dEntityExtEnvPowerIndex": dEntityExtEnvPowerIndex,
       "dEntityExtEnvPowerDescr": dEntityExtEnvPowerDescr,
       "dEntityExtEnvPowerUsedPower": dEntityExtEnvPowerUsedPower,
       "dEntityExtEnvPowerMaxPower": dEntityExtEnvPowerMaxPower,
       "dEntityExtEnvPowerStatus": dEntityExtEnvPowerStatus,
       "dEntityExtEnvAirFlowTable": dEntityExtEnvAirFlowTable,
       "dEntityExtEnvAirFlowEntry": dEntityExtEnvAirFlowEntry,
       "dEntityExtEnvAirFlowUnitId": dEntityExtEnvAirFlowUnitId,
       "dEntityExtEnvAirFlowStatus": dEntityExtEnvAirFlowStatus,
       "dEntityExtEnvTrap": dEntityExtEnvTrap,
       "dEntityExtEnvNotifyEnable": dEntityExtEnvNotifyEnable,
       "dEntityExtUnitTable": dEntityExtUnitTable,
       "dEntityExtUnitEntry": dEntityExtUnitEntry,
       "dEntityExtUnitIndex": dEntityExtUnitIndex,
       "dEntityExtUnitStatus": dEntityExtUnitStatus,
       "dEntityExtUnitUpTime": dEntityExtUnitUpTime,
       "dEntityExtMemoryUtilTable": dEntityExtMemoryUtilTable,
       "dEntityExtMemoryUtilEntry": dEntityExtMemoryUtilEntry,
       "dEntityExtMemUtilUnitId": dEntityExtMemUtilUnitId,
       "dEntityExtMemUtilType": dEntityExtMemUtilType,
       "dEntityExtMemUtilTotal": dEntityExtMemUtilTotal,
       "dEntityExtMemUtilUsed": dEntityExtMemUtilUsed,
       "dEntityExtMemUtilFree": dEntityExtMemUtilFree,
       "dEntityExtCpuUtilTable": dEntityExtCpuUtilTable,
       "dEntityExtCpuUtilEntry": dEntityExtCpuUtilEntry,
       "dEntityExtCpuUtilUnitId": dEntityExtCpuUtilUnitId,
       "dEntityExtCpuUtilCpuID": dEntityExtCpuUtilCpuID,
       "dEntityExtCpuUtilFiveSeconds": dEntityExtCpuUtilFiveSeconds,
       "dEntityExtCpuUtilOneMinute": dEntityExtCpuUtilOneMinute,
       "dEntityExtCpuUtilFiveMinutes": dEntityExtCpuUtilFiveMinutes,
       "dEntityExtVersionTable": dEntityExtVersionTable,
       "dEntityExtVersionEntry": dEntityExtVersionEntry,
       "dEntityExtVersionUnitId": dEntityExtVersionUnitId,
       "dEntityExtVersionBootloader": dEntityExtVersionBootloader,
       "dEntityExtVersionRuntime": dEntityExtVersionRuntime,
       "dEntityExtConformance": dEntityExtConformance,
       "dEntityExtMIBCompliances": dEntityExtMIBCompliances,
       "dEntityExtCompliance": dEntityExtCompliance,
       "dEntityExtMIBGroups": dEntityExtMIBGroups,
       "dEntityExtTempGroup": dEntityExtTempGroup,
       "dEntityExtFanGroup": dEntityExtFanGroup,
       "dEntityExtPowerGroup": dEntityExtPowerGroup,
       "dEntityExtSystemInfoGroup": dEntityExtSystemInfoGroup,
       "dEntityExtGenericNotifInfoGroup": dEntityExtGenericNotifInfoGroup,
       "dEntityExtFanNotifGroup": dEntityExtFanNotifGroup,
       "dEntityExtThermalNotifGroup": dEntityExtThermalNotifGroup,
       "dEntityExtPowerNotifGroup": dEntityExtPowerNotifGroup,
       "dEntityExtAirFlowNotifGroup": dEntityExtAirFlowNotifGroup,
       "dEntityExtFactoryResetButtonNotifGroup": dEntityExtFactoryResetButtonNotifGroup}
)
