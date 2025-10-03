# SNMP MIB module (EXTREME-ENTITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\extreme\EXTREME-ENTITY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:43:26 2025
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

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

extremeEntity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 31)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeEntityFRUTable_Object = MibTable
extremeEntityFRUTable = _ExtremeEntityFRUTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 31, 1)
)
if mibBuilder.loadTexts:
    extremeEntityFRUTable.setStatus("current")
_ExtremeEntityFRUEntry_Object = MibTableRow
extremeEntityFRUEntry = _ExtremeEntityFRUEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 31, 1, 1)
)
extremeEntityFRUEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    extremeEntityFRUEntry.setStatus("current")
_ExtremeEntityFRUStartTime_Type = Unsigned32
_ExtremeEntityFRUStartTime_Object = MibTableColumn
extremeEntityFRUStartTime = _ExtremeEntityFRUStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 31, 1, 1, 1),
    _ExtremeEntityFRUStartTime_Type()
)
extremeEntityFRUStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEntityFRUStartTime.setStatus("current")
_ExtremeEntityFRUOdometer_Type = Unsigned32
_ExtremeEntityFRUOdometer_Object = MibTableColumn
extremeEntityFRUOdometer = _ExtremeEntityFRUOdometer_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 31, 1, 1, 2),
    _ExtremeEntityFRUOdometer_Type()
)
extremeEntityFRUOdometer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEntityFRUOdometer.setStatus("current")


class _ExtremeEntityFRUOdometerUnit_Type(Integer32):
    """Custom type extremeEntityFRUOdometerUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("days", 1),
          ("seconds", 2))
    )


_ExtremeEntityFRUOdometerUnit_Type.__name__ = "Integer32"
_ExtremeEntityFRUOdometerUnit_Object = MibTableColumn
extremeEntityFRUOdometerUnit = _ExtremeEntityFRUOdometerUnit_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 31, 1, 1, 3),
    _ExtremeEntityFRUOdometerUnit_Type()
)
extremeEntityFRUOdometerUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEntityFRUOdometerUnit.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-ENTITY-MIB",
    **{"extremeEntity": extremeEntity,
       "extremeEntityFRUTable": extremeEntityFRUTable,
       "extremeEntityFRUEntry": extremeEntityFRUEntry,
       "extremeEntityFRUStartTime": extremeEntityFRUStartTime,
       "extremeEntityFRUOdometer": extremeEntityFRUOdometer,
       "extremeEntityFRUOdometerUnit": extremeEntityFRUOdometerUnit}
)
