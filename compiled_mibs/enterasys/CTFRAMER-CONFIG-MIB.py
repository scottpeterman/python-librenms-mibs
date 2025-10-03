# SNMP MIB module (CTFRAMER-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\enterasys\CTFRAMER-CONFIG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:40:22 2025
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

(ctFramerConfig,
 ctIfPortPortNumber) = mibBuilder.importSymbols(
    "CTIF-EXT-MIB",
    "ctFramerConfig",
    "ctIfPortPortNumber")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtFramerBaseConfig_ObjectIdentity = ObjectIdentity
ctFramerBaseConfig = _CtFramerBaseConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1)
)
_CtFramerConfigTable_Object = MibTable
ctFramerConfigTable = _CtFramerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1, 1)
)
if mibBuilder.loadTexts:
    ctFramerConfigTable.setStatus("mandatory")
_CtFramerConfigEntry_Object = MibTableRow
ctFramerConfigEntry = _CtFramerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1, 1, 1)
)
ctFramerConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CTIF-EXT-MIB", "ctIfPortPortNumber"),
)
if mibBuilder.loadTexts:
    ctFramerConfigEntry.setStatus("mandatory")


class _CtFramerStatsConfig_Type(Integer32):
    """Custom type ctFramerStatsConfig based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_CtFramerStatsConfig_Type.__name__ = "Integer32"
_CtFramerStatsConfig_Object = MibTableColumn
ctFramerStatsConfig = _CtFramerStatsConfig_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1, 1, 1, 1),
    _CtFramerStatsConfig_Type()
)
ctFramerStatsConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctFramerStatsConfig.setStatus("mandatory")


class _CtFramerAlarmsConfig_Type(Integer32):
    """Custom type ctFramerAlarmsConfig based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_CtFramerAlarmsConfig_Type.__name__ = "Integer32"
_CtFramerAlarmsConfig_Object = MibTableColumn
ctFramerAlarmsConfig = _CtFramerAlarmsConfig_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1, 1, 1, 2),
    _CtFramerAlarmsConfig_Type()
)
ctFramerAlarmsConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctFramerAlarmsConfig.setStatus("mandatory")


class _CtFramerMediumConfig_Type(Integer32):
    """Custom type ctFramerMediumConfig based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sonet", 1),
          ("sdh", 2))
    )


_CtFramerMediumConfig_Type.__name__ = "Integer32"
_CtFramerMediumConfig_Object = MibTableColumn
ctFramerMediumConfig = _CtFramerMediumConfig_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1, 1, 1, 3),
    _CtFramerMediumConfig_Type()
)
ctFramerMediumConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctFramerMediumConfig.setStatus("mandatory")


class _CtFramerIdleCellsConfig_Type(Integer32):
    """Custom type ctFramerIdleCellsConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("unassigned", 2))
    )


_CtFramerIdleCellsConfig_Type.__name__ = "Integer32"
_CtFramerIdleCellsConfig_Object = MibTableColumn
ctFramerIdleCellsConfig = _CtFramerIdleCellsConfig_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1, 1, 1, 4),
    _CtFramerIdleCellsConfig_Type()
)
ctFramerIdleCellsConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctFramerIdleCellsConfig.setStatus("mandatory")


class _CtFramerCellPayScramConfig_Type(Integer32):
    """Custom type ctFramerCellPayScramConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_CtFramerCellPayScramConfig_Type.__name__ = "Integer32"
_CtFramerCellPayScramConfig_Object = MibTableColumn
ctFramerCellPayScramConfig = _CtFramerCellPayScramConfig_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1, 1, 1, 5),
    _CtFramerCellPayScramConfig_Type()
)
ctFramerCellPayScramConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctFramerCellPayScramConfig.setStatus("mandatory")
_CtFramerSonetConfig_ObjectIdentity = ObjectIdentity
ctFramerSonetConfig = _CtFramerSonetConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 2)
)
_CtFramerDS3Config_ObjectIdentity = ObjectIdentity
ctFramerDS3Config = _CtFramerDS3Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTFRAMER-CONFIG-MIB",
    **{"ctFramerBaseConfig": ctFramerBaseConfig,
       "ctFramerConfigTable": ctFramerConfigTable,
       "ctFramerConfigEntry": ctFramerConfigEntry,
       "ctFramerStatsConfig": ctFramerStatsConfig,
       "ctFramerAlarmsConfig": ctFramerAlarmsConfig,
       "ctFramerMediumConfig": ctFramerMediumConfig,
       "ctFramerIdleCellsConfig": ctFramerIdleCellsConfig,
       "ctFramerCellPayScramConfig": ctFramerCellPayScramConfig,
       "ctFramerSonetConfig": ctFramerSonetConfig,
       "ctFramerDS3Config": ctFramerDS3Config}
)
