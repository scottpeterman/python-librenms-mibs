# SNMP MIB module (AT-PLUGGABLE-DIAGNOSTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\awplus\AT-PLUGGABLE-DIAGNOSTICS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:20:33 2025
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

(DisplayStringUnsized,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "DisplayStringUnsized")

(sysinfo,) = mibBuilder.importSymbols(
    "AT-SYSINFO-MIB",
    "sysinfo")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

atPluggableDiag = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28)
)
if mibBuilder.loadTexts:
    atPluggableDiag.setRevisions(
        ("2015-07-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtPluggableDiagTable_ObjectIdentity = ObjectIdentity
atPluggableDiagTable = _AtPluggableDiagTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1)
)
_AtPluggableDiagTempTable_Object = MibTable
atPluggableDiagTempTable = _AtPluggableDiagTempTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1)
)
if mibBuilder.loadTexts:
    atPluggableDiagTempTable.setStatus("current")
_AtPluggableDiagTempEntry_Object = MibTableRow
atPluggableDiagTempEntry = _AtPluggableDiagTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1)
)
atPluggableDiagTempEntry.setIndexNames(
    (0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagTempIfIndex"),
    (0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagTempChannel"),
)
if mibBuilder.loadTexts:
    atPluggableDiagTempEntry.setStatus("current")
_AtPluggableDiagTempIfIndex_Type = InterfaceIndex
_AtPluggableDiagTempIfIndex_Object = MibTableColumn
atPluggableDiagTempIfIndex = _AtPluggableDiagTempIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1, 1),
    _AtPluggableDiagTempIfIndex_Type()
)
atPluggableDiagTempIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atPluggableDiagTempIfIndex.setStatus("current")


class _AtPluggableDiagTempChannel_Type(Integer32):
    """Custom type atPluggableDiagTempChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AtPluggableDiagTempChannel_Type.__name__ = "Integer32"
_AtPluggableDiagTempChannel_Object = MibTableColumn
atPluggableDiagTempChannel = _AtPluggableDiagTempChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1, 2),
    _AtPluggableDiagTempChannel_Type()
)
atPluggableDiagTempChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atPluggableDiagTempChannel.setStatus("current")
_AtPluggableDiagTempStatusReading_Type = Integer32
_AtPluggableDiagTempStatusReading_Object = MibTableColumn
atPluggableDiagTempStatusReading = _AtPluggableDiagTempStatusReading_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1, 3),
    _AtPluggableDiagTempStatusReading_Type()
)
atPluggableDiagTempStatusReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagTempStatusReading.setStatus("current")
if mibBuilder.loadTexts:
    atPluggableDiagTempStatusReading.setUnits("0.001 degree C")
_AtPluggableDiagTempCurrentAlarm_Type = OctetString
_AtPluggableDiagTempCurrentAlarm_Object = MibTableColumn
atPluggableDiagTempCurrentAlarm = _AtPluggableDiagTempCurrentAlarm_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1, 4),
    _AtPluggableDiagTempCurrentAlarm_Type()
)
atPluggableDiagTempCurrentAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagTempCurrentAlarm.setStatus("current")
_AtPluggableDiagTempAlarmMax_Type = Integer32
_AtPluggableDiagTempAlarmMax_Object = MibTableColumn
atPluggableDiagTempAlarmMax = _AtPluggableDiagTempAlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1, 5),
    _AtPluggableDiagTempAlarmMax_Type()
)
atPluggableDiagTempAlarmMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagTempAlarmMax.setStatus("current")
if mibBuilder.loadTexts:
    atPluggableDiagTempAlarmMax.setUnits("0.001 degree C")
_AtPluggableDiagTempAlarmMin_Type = Integer32
_AtPluggableDiagTempAlarmMin_Object = MibTableColumn
atPluggableDiagTempAlarmMin = _AtPluggableDiagTempAlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1, 6),
    _AtPluggableDiagTempAlarmMin_Type()
)
atPluggableDiagTempAlarmMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagTempAlarmMin.setStatus("current")
if mibBuilder.loadTexts:
    atPluggableDiagTempAlarmMin.setUnits("0.001 degree C")
_AtPluggableDiagTempCurrentWarning_Type = OctetString
_AtPluggableDiagTempCurrentWarning_Object = MibTableColumn
atPluggableDiagTempCurrentWarning = _AtPluggableDiagTempCurrentWarning_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1, 7),
    _AtPluggableDiagTempCurrentWarning_Type()
)
atPluggableDiagTempCurrentWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagTempCurrentWarning.setStatus("current")
_AtPluggableDiagTempWarningMax_Type = Integer32
_AtPluggableDiagTempWarningMax_Object = MibTableColumn
atPluggableDiagTempWarningMax = _AtPluggableDiagTempWarningMax_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1, 8),
    _AtPluggableDiagTempWarningMax_Type()
)
atPluggableDiagTempWarningMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagTempWarningMax.setStatus("current")
if mibBuilder.loadTexts:
    atPluggableDiagTempWarningMax.setUnits("0.001 degree C")
_AtPluggableDiagTempWarningMin_Type = Integer32
_AtPluggableDiagTempWarningMin_Object = MibTableColumn
atPluggableDiagTempWarningMin = _AtPluggableDiagTempWarningMin_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1, 9),
    _AtPluggableDiagTempWarningMin_Type()
)
atPluggableDiagTempWarningMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagTempWarningMin.setStatus("current")
if mibBuilder.loadTexts:
    atPluggableDiagTempWarningMin.setUnits("0.001 degree C")
_AtPluggableDiagVccTable_Object = MibTable
atPluggableDiagVccTable = _AtPluggableDiagVccTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2)
)
if mibBuilder.loadTexts:
    atPluggableDiagVccTable.setStatus("current")
_AtPluggableDiagVccEntry_Object = MibTableRow
atPluggableDiagVccEntry = _AtPluggableDiagVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1)
)
atPluggableDiagVccEntry.setIndexNames(
    (0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagVccIfIndex"),
    (0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagVccChannel"),
)
if mibBuilder.loadTexts:
    atPluggableDiagVccEntry.setStatus("current")
_AtPluggableDiagVccIfIndex_Type = InterfaceIndex
_AtPluggableDiagVccIfIndex_Object = MibTableColumn
atPluggableDiagVccIfIndex = _AtPluggableDiagVccIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1, 1),
    _AtPluggableDiagVccIfIndex_Type()
)
atPluggableDiagVccIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atPluggableDiagVccIfIndex.setStatus("current")


class _AtPluggableDiagVccChannel_Type(Integer32):
    """Custom type atPluggableDiagVccChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AtPluggableDiagVccChannel_Type.__name__ = "Integer32"
_AtPluggableDiagVccChannel_Object = MibTableColumn
atPluggableDiagVccChannel = _AtPluggableDiagVccChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1, 2),
    _AtPluggableDiagVccChannel_Type()
)
atPluggableDiagVccChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atPluggableDiagVccChannel.setStatus("current")
_AtPluggableDiagVccStatusReading_Type = Integer32
_AtPluggableDiagVccStatusReading_Object = MibTableColumn
atPluggableDiagVccStatusReading = _AtPluggableDiagVccStatusReading_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1, 3),
    _AtPluggableDiagVccStatusReading_Type()
)
atPluggableDiagVccStatusReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagVccStatusReading.setStatus("current")
if mibBuilder.loadTexts:
    atPluggableDiagVccStatusReading.setUnits("0.0001 volts")
_AtPluggableDiagVccCurrentAlarm_Type = OctetString
_AtPluggableDiagVccCurrentAlarm_Object = MibTableColumn
atPluggableDiagVccCurrentAlarm = _AtPluggableDiagVccCurrentAlarm_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1, 4),
    _AtPluggableDiagVccCurrentAlarm_Type()
)
atPluggableDiagVccCurrentAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagVccCurrentAlarm.setStatus("current")
_AtPluggableDiagVccAlarmMax_Type = Integer32
_AtPluggableDiagVccAlarmMax_Object = MibTableColumn
atPluggableDiagVccAlarmMax = _AtPluggableDiagVccAlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1, 5),
    _AtPluggableDiagVccAlarmMax_Type()
)
atPluggableDiagVccAlarmMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagVccAlarmMax.setStatus("current")
if mibBuilder.loadTexts:
    atPluggableDiagVccAlarmMax.setUnits("0.0001 volts")
_AtPluggableDiagVccAlarmMin_Type = Integer32
_AtPluggableDiagVccAlarmMin_Object = MibTableColumn
atPluggableDiagVccAlarmMin = _AtPluggableDiagVccAlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1, 6),
    _AtPluggableDiagVccAlarmMin_Type()
)
atPluggableDiagVccAlarmMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagVccAlarmMin.setStatus("current")
if mibBuilder.loadTexts:
    atPluggableDiagVccAlarmMin.setUnits("0.0001 volts")
_AtPluggableDiagVccCurrentWarning_Type = OctetString
_AtPluggableDiagVccCurrentWarning_Object = MibTableColumn
atPluggableDiagVccCurrentWarning = _AtPluggableDiagVccCurrentWarning_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1, 7),
    _AtPluggableDiagVccCurrentWarning_Type()
)
atPluggableDiagVccCurrentWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagVccCurrentWarning.setStatus("current")
_AtPluggableDiagVccWarningMax_Type = Integer32
_AtPluggableDiagVccWarningMax_Object = MibTableColumn
atPluggableDiagVccWarningMax = _AtPluggableDiagVccWarningMax_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1, 8),
    _AtPluggableDiagVccWarningMax_Type()
)
atPluggableDiagVccWarningMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagVccWarningMax.setStatus("current")
if mibBuilder.loadTexts:
    atPluggableDiagVccWarningMax.setUnits("0.0001 volts")
_AtPluggableDiagVccWarningMin_Type = Integer32
_AtPluggableDiagVccWarningMin_Object = MibTableColumn
atPluggableDiagVccWarningMin = _AtPluggableDiagVccWarningMin_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1, 9),
    _AtPluggableDiagVccWarningMin_Type()
)
atPluggableDiagVccWarningMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagVccWarningMin.setStatus("current")
if mibBuilder.loadTexts:
    atPluggableDiagVccWarningMin.setUnits("0.0001 volts")
_AtPluggableDiagTxBiasTable_Object = MibTable
atPluggableDiagTxBiasTable = _AtPluggableDiagTxBiasTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3)
)
if mibBuilder.loadTexts:
    atPluggableDiagTxBiasTable.setStatus("current")
_AtPluggableDiagTxBiasEntry_Object = MibTableRow
atPluggableDiagTxBiasEntry = _AtPluggableDiagTxBiasEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1)
)
atPluggableDiagTxBiasEntry.setIndexNames(
    (0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagTxBiasIfIndex"),
    (0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagTxBiasChannel"),
)
if mibBuilder.loadTexts:
    atPluggableDiagTxBiasEntry.setStatus("current")
_AtPluggableDiagTxBiasIfIndex_Type = InterfaceIndex
_AtPluggableDiagTxBiasIfIndex_Object = MibTableColumn
atPluggableDiagTxBiasIfIndex = _AtPluggableDiagTxBiasIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1, 1),
    _AtPluggableDiagTxBiasIfIndex_Type()
)
atPluggableDiagTxBiasIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atPluggableDiagTxBiasIfIndex.setStatus("current")


class _AtPluggableDiagTxBiasChannel_Type(Integer32):
    """Custom type atPluggableDiagTxBiasChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AtPluggableDiagTxBiasChannel_Type.__name__ = "Integer32"
_AtPluggableDiagTxBiasChannel_Object = MibTableColumn
atPluggableDiagTxBiasChannel = _AtPluggableDiagTxBiasChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1, 2),
    _AtPluggableDiagTxBiasChannel_Type()
)
atPluggableDiagTxBiasChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atPluggableDiagTxBiasChannel.setStatus("current")
_AtPluggableDiagTxBiasStatusReading_Type = Integer32
_AtPluggableDiagTxBiasStatusReading_Object = MibTableColumn
atPluggableDiagTxBiasStatusReading = _AtPluggableDiagTxBiasStatusReading_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1, 3),
    _AtPluggableDiagTxBiasStatusReading_Type()
)
atPluggableDiagTxBiasStatusReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagTxBiasStatusReading.setStatus("current")
if mibBuilder.loadTexts:
    atPluggableDiagTxBiasStatusReading.setUnits("0.001 mA")
_AtPluggableDiagTxBiasCurrentAlarm_Type = OctetString
_AtPluggableDiagTxBiasCurrentAlarm_Object = MibTableColumn
atPluggableDiagTxBiasCurrentAlarm = _AtPluggableDiagTxBiasCurrentAlarm_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1, 4),
    _AtPluggableDiagTxBiasCurrentAlarm_Type()
)
atPluggableDiagTxBiasCurrentAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagTxBiasCurrentAlarm.setStatus("current")
_AtPluggableDiagTxBiasAlarmMax_Type = Integer32
_AtPluggableDiagTxBiasAlarmMax_Object = MibTableColumn
atPluggableDiagTxBiasAlarmMax = _AtPluggableDiagTxBiasAlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1, 5),
    _AtPluggableDiagTxBiasAlarmMax_Type()
)
atPluggableDiagTxBiasAlarmMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagTxBiasAlarmMax.setStatus("current")
if mibBuilder.loadTexts:
    atPluggableDiagTxBiasAlarmMax.setUnits("0.001 mA")
_AtPluggableDiagTxBiasAlarmMin_Type = Integer32
_AtPluggableDiagTxBiasAlarmMin_Object = MibTableColumn
atPluggableDiagTxBiasAlarmMin = _AtPluggableDiagTxBiasAlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1, 6),
    _AtPluggableDiagTxBiasAlarmMin_Type()
)
atPluggableDiagTxBiasAlarmMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagTxBiasAlarmMin.setStatus("current")
if mibBuilder.loadTexts:
    atPluggableDiagTxBiasAlarmMin.setUnits("0.001 mA")
_AtPluggableDiagTxBiasCurrentWarning_Type = OctetString
_AtPluggableDiagTxBiasCurrentWarning_Object = MibTableColumn
atPluggableDiagTxBiasCurrentWarning = _AtPluggableDiagTxBiasCurrentWarning_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1, 7),
    _AtPluggableDiagTxBiasCurrentWarning_Type()
)
atPluggableDiagTxBiasCurrentWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagTxBiasCurrentWarning.setStatus("current")
_AtPluggableDiagTxBiasWarningMax_Type = Integer32
_AtPluggableDiagTxBiasWarningMax_Object = MibTableColumn
atPluggableDiagTxBiasWarningMax = _AtPluggableDiagTxBiasWarningMax_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1, 8),
    _AtPluggableDiagTxBiasWarningMax_Type()
)
atPluggableDiagTxBiasWarningMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagTxBiasWarningMax.setStatus("current")
if mibBuilder.loadTexts:
    atPluggableDiagTxBiasWarningMax.setUnits("0.001 mA")
_AtPluggableDiagTxBiasWarningMin_Type = Integer32
_AtPluggableDiagTxBiasWarningMin_Object = MibTableColumn
atPluggableDiagTxBiasWarningMin = _AtPluggableDiagTxBiasWarningMin_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1, 9),
    _AtPluggableDiagTxBiasWarningMin_Type()
)
atPluggableDiagTxBiasWarningMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagTxBiasWarningMin.setStatus("current")
if mibBuilder.loadTexts:
    atPluggableDiagTxBiasWarningMin.setUnits("0.001 mA")
_AtPluggableDiagTxPowerTable_Object = MibTable
atPluggableDiagTxPowerTable = _AtPluggableDiagTxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4)
)
if mibBuilder.loadTexts:
    atPluggableDiagTxPowerTable.setStatus("current")
_AtPluggableDiagTxPowerEntry_Object = MibTableRow
atPluggableDiagTxPowerEntry = _AtPluggableDiagTxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1)
)
atPluggableDiagTxPowerEntry.setIndexNames(
    (0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagTxPowerIfIndex"),
    (0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagTxPowerChannel"),
)
if mibBuilder.loadTexts:
    atPluggableDiagTxPowerEntry.setStatus("current")
_AtPluggableDiagTxPowerIfIndex_Type = InterfaceIndex
_AtPluggableDiagTxPowerIfIndex_Object = MibTableColumn
atPluggableDiagTxPowerIfIndex = _AtPluggableDiagTxPowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1, 1),
    _AtPluggableDiagTxPowerIfIndex_Type()
)
atPluggableDiagTxPowerIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atPluggableDiagTxPowerIfIndex.setStatus("current")


class _AtPluggableDiagTxPowerChannel_Type(Integer32):
    """Custom type atPluggableDiagTxPowerChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AtPluggableDiagTxPowerChannel_Type.__name__ = "Integer32"
_AtPluggableDiagTxPowerChannel_Object = MibTableColumn
atPluggableDiagTxPowerChannel = _AtPluggableDiagTxPowerChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1, 2),
    _AtPluggableDiagTxPowerChannel_Type()
)
atPluggableDiagTxPowerChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atPluggableDiagTxPowerChannel.setStatus("current")
_AtPluggableDiagTxPowerStatusReading_Type = Integer32
_AtPluggableDiagTxPowerStatusReading_Object = MibTableColumn
atPluggableDiagTxPowerStatusReading = _AtPluggableDiagTxPowerStatusReading_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1, 3),
    _AtPluggableDiagTxPowerStatusReading_Type()
)
atPluggableDiagTxPowerStatusReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagTxPowerStatusReading.setStatus("current")
if mibBuilder.loadTexts:
    atPluggableDiagTxPowerStatusReading.setUnits("0.0001 mW")
_AtPluggableDiagTxPowerCurrentAlarm_Type = OctetString
_AtPluggableDiagTxPowerCurrentAlarm_Object = MibTableColumn
atPluggableDiagTxPowerCurrentAlarm = _AtPluggableDiagTxPowerCurrentAlarm_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1, 4),
    _AtPluggableDiagTxPowerCurrentAlarm_Type()
)
atPluggableDiagTxPowerCurrentAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagTxPowerCurrentAlarm.setStatus("current")
_AtPluggableDiagTxPowerAlarmMax_Type = Integer32
_AtPluggableDiagTxPowerAlarmMax_Object = MibTableColumn
atPluggableDiagTxPowerAlarmMax = _AtPluggableDiagTxPowerAlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1, 5),
    _AtPluggableDiagTxPowerAlarmMax_Type()
)
atPluggableDiagTxPowerAlarmMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagTxPowerAlarmMax.setStatus("current")
if mibBuilder.loadTexts:
    atPluggableDiagTxPowerAlarmMax.setUnits("0.0001 mW")
_AtPluggableDiagTxPowerAlarmMin_Type = Integer32
_AtPluggableDiagTxPowerAlarmMin_Object = MibTableColumn
atPluggableDiagTxPowerAlarmMin = _AtPluggableDiagTxPowerAlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1, 6),
    _AtPluggableDiagTxPowerAlarmMin_Type()
)
atPluggableDiagTxPowerAlarmMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagTxPowerAlarmMin.setStatus("current")
if mibBuilder.loadTexts:
    atPluggableDiagTxPowerAlarmMin.setUnits("0.0001 mW")
_AtPluggableDiagTxPowerCurrentWarning_Type = OctetString
_AtPluggableDiagTxPowerCurrentWarning_Object = MibTableColumn
atPluggableDiagTxPowerCurrentWarning = _AtPluggableDiagTxPowerCurrentWarning_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1, 7),
    _AtPluggableDiagTxPowerCurrentWarning_Type()
)
atPluggableDiagTxPowerCurrentWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagTxPowerCurrentWarning.setStatus("current")
_AtPluggableDiagTxPowerWarningMax_Type = Integer32
_AtPluggableDiagTxPowerWarningMax_Object = MibTableColumn
atPluggableDiagTxPowerWarningMax = _AtPluggableDiagTxPowerWarningMax_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1, 8),
    _AtPluggableDiagTxPowerWarningMax_Type()
)
atPluggableDiagTxPowerWarningMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagTxPowerWarningMax.setStatus("current")
if mibBuilder.loadTexts:
    atPluggableDiagTxPowerWarningMax.setUnits("0.0001 mW")
_AtPluggableDiagTxPowerWarningMin_Type = Integer32
_AtPluggableDiagTxPowerWarningMin_Object = MibTableColumn
atPluggableDiagTxPowerWarningMin = _AtPluggableDiagTxPowerWarningMin_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1, 9),
    _AtPluggableDiagTxPowerWarningMin_Type()
)
atPluggableDiagTxPowerWarningMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagTxPowerWarningMin.setStatus("current")
if mibBuilder.loadTexts:
    atPluggableDiagTxPowerWarningMin.setUnits("0.0001 mW")
_AtPluggableDiagRxPowerTable_Object = MibTable
atPluggableDiagRxPowerTable = _AtPluggableDiagRxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5)
)
if mibBuilder.loadTexts:
    atPluggableDiagRxPowerTable.setStatus("current")
_AtPluggableDiagRxPowerEntry_Object = MibTableRow
atPluggableDiagRxPowerEntry = _AtPluggableDiagRxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1)
)
atPluggableDiagRxPowerEntry.setIndexNames(
    (0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagRxPowerIfIndex"),
    (0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagRxPowerChannel"),
)
if mibBuilder.loadTexts:
    atPluggableDiagRxPowerEntry.setStatus("current")
_AtPluggableDiagRxPowerIfIndex_Type = InterfaceIndex
_AtPluggableDiagRxPowerIfIndex_Object = MibTableColumn
atPluggableDiagRxPowerIfIndex = _AtPluggableDiagRxPowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1, 1),
    _AtPluggableDiagRxPowerIfIndex_Type()
)
atPluggableDiagRxPowerIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atPluggableDiagRxPowerIfIndex.setStatus("current")


class _AtPluggableDiagRxPowerChannel_Type(Integer32):
    """Custom type atPluggableDiagRxPowerChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AtPluggableDiagRxPowerChannel_Type.__name__ = "Integer32"
_AtPluggableDiagRxPowerChannel_Object = MibTableColumn
atPluggableDiagRxPowerChannel = _AtPluggableDiagRxPowerChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1, 2),
    _AtPluggableDiagRxPowerChannel_Type()
)
atPluggableDiagRxPowerChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atPluggableDiagRxPowerChannel.setStatus("current")
_AtPluggableDiagRxPowerStatusReading_Type = Integer32
_AtPluggableDiagRxPowerStatusReading_Object = MibTableColumn
atPluggableDiagRxPowerStatusReading = _AtPluggableDiagRxPowerStatusReading_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1, 3),
    _AtPluggableDiagRxPowerStatusReading_Type()
)
atPluggableDiagRxPowerStatusReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagRxPowerStatusReading.setStatus("current")
if mibBuilder.loadTexts:
    atPluggableDiagRxPowerStatusReading.setUnits("0.0001 mW")
_AtPluggableDiagRxPowerCurrentAlarm_Type = OctetString
_AtPluggableDiagRxPowerCurrentAlarm_Object = MibTableColumn
atPluggableDiagRxPowerCurrentAlarm = _AtPluggableDiagRxPowerCurrentAlarm_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1, 4),
    _AtPluggableDiagRxPowerCurrentAlarm_Type()
)
atPluggableDiagRxPowerCurrentAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagRxPowerCurrentAlarm.setStatus("current")
_AtPluggableDiagRxPowerAlarmMax_Type = Integer32
_AtPluggableDiagRxPowerAlarmMax_Object = MibTableColumn
atPluggableDiagRxPowerAlarmMax = _AtPluggableDiagRxPowerAlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1, 5),
    _AtPluggableDiagRxPowerAlarmMax_Type()
)
atPluggableDiagRxPowerAlarmMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagRxPowerAlarmMax.setStatus("current")
if mibBuilder.loadTexts:
    atPluggableDiagRxPowerAlarmMax.setUnits("0.0001 mW")
_AtPluggableDiagRxPowerAlarmMin_Type = Integer32
_AtPluggableDiagRxPowerAlarmMin_Object = MibTableColumn
atPluggableDiagRxPowerAlarmMin = _AtPluggableDiagRxPowerAlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1, 6),
    _AtPluggableDiagRxPowerAlarmMin_Type()
)
atPluggableDiagRxPowerAlarmMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagRxPowerAlarmMin.setStatus("current")
if mibBuilder.loadTexts:
    atPluggableDiagRxPowerAlarmMin.setUnits("0.0001 mW")
_AtPluggableDiagRxPowerCurrentWarning_Type = OctetString
_AtPluggableDiagRxPowerCurrentWarning_Object = MibTableColumn
atPluggableDiagRxPowerCurrentWarning = _AtPluggableDiagRxPowerCurrentWarning_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1, 7),
    _AtPluggableDiagRxPowerCurrentWarning_Type()
)
atPluggableDiagRxPowerCurrentWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagRxPowerCurrentWarning.setStatus("current")
_AtPluggableDiagRxPowerWarningMax_Type = Integer32
_AtPluggableDiagRxPowerWarningMax_Object = MibTableColumn
atPluggableDiagRxPowerWarningMax = _AtPluggableDiagRxPowerWarningMax_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1, 8),
    _AtPluggableDiagRxPowerWarningMax_Type()
)
atPluggableDiagRxPowerWarningMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagRxPowerWarningMax.setStatus("current")
if mibBuilder.loadTexts:
    atPluggableDiagRxPowerWarningMax.setUnits("0.0001 mW")
_AtPluggableDiagRxPowerWarningMin_Type = Integer32
_AtPluggableDiagRxPowerWarningMin_Object = MibTableColumn
atPluggableDiagRxPowerWarningMin = _AtPluggableDiagRxPowerWarningMin_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1, 9),
    _AtPluggableDiagRxPowerWarningMin_Type()
)
atPluggableDiagRxPowerWarningMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagRxPowerWarningMin.setStatus("current")
if mibBuilder.loadTexts:
    atPluggableDiagRxPowerWarningMin.setUnits("0.0001 mW")
_AtPluggableDiagRxLosTable_Object = MibTable
atPluggableDiagRxLosTable = _AtPluggableDiagRxLosTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 6)
)
if mibBuilder.loadTexts:
    atPluggableDiagRxLosTable.setStatus("current")
_AtPluggableDiagRxLosEntry_Object = MibTableRow
atPluggableDiagRxLosEntry = _AtPluggableDiagRxLosEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 6, 1)
)
atPluggableDiagRxLosEntry.setIndexNames(
    (0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagRxLosIfIndex"),
    (0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagRxLosChannel"),
)
if mibBuilder.loadTexts:
    atPluggableDiagRxLosEntry.setStatus("current")
_AtPluggableDiagRxLosIfIndex_Type = InterfaceIndex
_AtPluggableDiagRxLosIfIndex_Object = MibTableColumn
atPluggableDiagRxLosIfIndex = _AtPluggableDiagRxLosIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 6, 1, 1),
    _AtPluggableDiagRxLosIfIndex_Type()
)
atPluggableDiagRxLosIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atPluggableDiagRxLosIfIndex.setStatus("current")


class _AtPluggableDiagRxLosChannel_Type(Integer32):
    """Custom type atPluggableDiagRxLosChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AtPluggableDiagRxLosChannel_Type.__name__ = "Integer32"
_AtPluggableDiagRxLosChannel_Object = MibTableColumn
atPluggableDiagRxLosChannel = _AtPluggableDiagRxLosChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 6, 1, 2),
    _AtPluggableDiagRxLosChannel_Type()
)
atPluggableDiagRxLosChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atPluggableDiagRxLosChannel.setStatus("current")
_AtPluggableDiagRxLosStatusReading_Type = OctetString
_AtPluggableDiagRxLosStatusReading_Object = MibTableColumn
atPluggableDiagRxLosStatusReading = _AtPluggableDiagRxLosStatusReading_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 6, 1, 3),
    _AtPluggableDiagRxLosStatusReading_Type()
)
atPluggableDiagRxLosStatusReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPluggableDiagRxLosStatusReading.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-PLUGGABLE-DIAGNOSTICS-MIB",
    **{"atPluggableDiag": atPluggableDiag,
       "atPluggableDiagTable": atPluggableDiagTable,
       "atPluggableDiagTempTable": atPluggableDiagTempTable,
       "atPluggableDiagTempEntry": atPluggableDiagTempEntry,
       "atPluggableDiagTempIfIndex": atPluggableDiagTempIfIndex,
       "atPluggableDiagTempChannel": atPluggableDiagTempChannel,
       "atPluggableDiagTempStatusReading": atPluggableDiagTempStatusReading,
       "atPluggableDiagTempCurrentAlarm": atPluggableDiagTempCurrentAlarm,
       "atPluggableDiagTempAlarmMax": atPluggableDiagTempAlarmMax,
       "atPluggableDiagTempAlarmMin": atPluggableDiagTempAlarmMin,
       "atPluggableDiagTempCurrentWarning": atPluggableDiagTempCurrentWarning,
       "atPluggableDiagTempWarningMax": atPluggableDiagTempWarningMax,
       "atPluggableDiagTempWarningMin": atPluggableDiagTempWarningMin,
       "atPluggableDiagVccTable": atPluggableDiagVccTable,
       "atPluggableDiagVccEntry": atPluggableDiagVccEntry,
       "atPluggableDiagVccIfIndex": atPluggableDiagVccIfIndex,
       "atPluggableDiagVccChannel": atPluggableDiagVccChannel,
       "atPluggableDiagVccStatusReading": atPluggableDiagVccStatusReading,
       "atPluggableDiagVccCurrentAlarm": atPluggableDiagVccCurrentAlarm,
       "atPluggableDiagVccAlarmMax": atPluggableDiagVccAlarmMax,
       "atPluggableDiagVccAlarmMin": atPluggableDiagVccAlarmMin,
       "atPluggableDiagVccCurrentWarning": atPluggableDiagVccCurrentWarning,
       "atPluggableDiagVccWarningMax": atPluggableDiagVccWarningMax,
       "atPluggableDiagVccWarningMin": atPluggableDiagVccWarningMin,
       "atPluggableDiagTxBiasTable": atPluggableDiagTxBiasTable,
       "atPluggableDiagTxBiasEntry": atPluggableDiagTxBiasEntry,
       "atPluggableDiagTxBiasIfIndex": atPluggableDiagTxBiasIfIndex,
       "atPluggableDiagTxBiasChannel": atPluggableDiagTxBiasChannel,
       "atPluggableDiagTxBiasStatusReading": atPluggableDiagTxBiasStatusReading,
       "atPluggableDiagTxBiasCurrentAlarm": atPluggableDiagTxBiasCurrentAlarm,
       "atPluggableDiagTxBiasAlarmMax": atPluggableDiagTxBiasAlarmMax,
       "atPluggableDiagTxBiasAlarmMin": atPluggableDiagTxBiasAlarmMin,
       "atPluggableDiagTxBiasCurrentWarning": atPluggableDiagTxBiasCurrentWarning,
       "atPluggableDiagTxBiasWarningMax": atPluggableDiagTxBiasWarningMax,
       "atPluggableDiagTxBiasWarningMin": atPluggableDiagTxBiasWarningMin,
       "atPluggableDiagTxPowerTable": atPluggableDiagTxPowerTable,
       "atPluggableDiagTxPowerEntry": atPluggableDiagTxPowerEntry,
       "atPluggableDiagTxPowerIfIndex": atPluggableDiagTxPowerIfIndex,
       "atPluggableDiagTxPowerChannel": atPluggableDiagTxPowerChannel,
       "atPluggableDiagTxPowerStatusReading": atPluggableDiagTxPowerStatusReading,
       "atPluggableDiagTxPowerCurrentAlarm": atPluggableDiagTxPowerCurrentAlarm,
       "atPluggableDiagTxPowerAlarmMax": atPluggableDiagTxPowerAlarmMax,
       "atPluggableDiagTxPowerAlarmMin": atPluggableDiagTxPowerAlarmMin,
       "atPluggableDiagTxPowerCurrentWarning": atPluggableDiagTxPowerCurrentWarning,
       "atPluggableDiagTxPowerWarningMax": atPluggableDiagTxPowerWarningMax,
       "atPluggableDiagTxPowerWarningMin": atPluggableDiagTxPowerWarningMin,
       "atPluggableDiagRxPowerTable": atPluggableDiagRxPowerTable,
       "atPluggableDiagRxPowerEntry": atPluggableDiagRxPowerEntry,
       "atPluggableDiagRxPowerIfIndex": atPluggableDiagRxPowerIfIndex,
       "atPluggableDiagRxPowerChannel": atPluggableDiagRxPowerChannel,
       "atPluggableDiagRxPowerStatusReading": atPluggableDiagRxPowerStatusReading,
       "atPluggableDiagRxPowerCurrentAlarm": atPluggableDiagRxPowerCurrentAlarm,
       "atPluggableDiagRxPowerAlarmMax": atPluggableDiagRxPowerAlarmMax,
       "atPluggableDiagRxPowerAlarmMin": atPluggableDiagRxPowerAlarmMin,
       "atPluggableDiagRxPowerCurrentWarning": atPluggableDiagRxPowerCurrentWarning,
       "atPluggableDiagRxPowerWarningMax": atPluggableDiagRxPowerWarningMax,
       "atPluggableDiagRxPowerWarningMin": atPluggableDiagRxPowerWarningMin,
       "atPluggableDiagRxLosTable": atPluggableDiagRxLosTable,
       "atPluggableDiagRxLosEntry": atPluggableDiagRxLosEntry,
       "atPluggableDiagRxLosIfIndex": atPluggableDiagRxLosIfIndex,
       "atPluggableDiagRxLosChannel": atPluggableDiagRxLosChannel,
       "atPluggableDiagRxLosStatusReading": atPluggableDiagRxLosStatusReading}
)
