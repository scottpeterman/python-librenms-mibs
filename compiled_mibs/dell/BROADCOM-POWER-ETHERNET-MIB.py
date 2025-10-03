# SNMP MIB module (BROADCOM-POWER-ETHERNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dell\BROADCOM-POWER-ETHERNET-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:29 2025
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

(fastPath,) = mibBuilder.importSymbols(
    "BROADCOM-REF-MIB",
    "fastPath")

(pethMainPseEntry,
 pethPsePortEntry) = mibBuilder.importSymbols(
    "POWER-ETHERNET-MIB",
    "pethMainPseEntry",
    "pethPsePortEntry")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fastPathpowerEthernetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15)
)
if mibBuilder.loadTexts:
    fastPathpowerEthernetMIB.setRevisions(
        ("2007-08-19 12:00",
         "2007-05-23 00:00",
         "2003-11-10 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentPethObjects_ObjectIdentity = ObjectIdentity
agentPethObjects = _AgentPethObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1)
)
_AgentPethPsePortTable_Object = MibTable
agentPethPsePortTable = _AgentPethPsePortTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 1)
)
if mibBuilder.loadTexts:
    agentPethPsePortTable.setStatus("current")
_AgentPethPsePortEntry_Object = MibTableRow
agentPethPsePortEntry = _AgentPethPsePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 1, 1)
)
if mibBuilder.loadTexts:
    agentPethPsePortEntry.setStatus("current")
_AgentPethPowerLimit_Type = Gauge32
_AgentPethPowerLimit_Object = MibTableColumn
agentPethPowerLimit = _AgentPethPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 1, 1, 1),
    _AgentPethPowerLimit_Type()
)
agentPethPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPethPowerLimit.setStatus("current")
if mibBuilder.loadTexts:
    agentPethPowerLimit.setUnits("Milliwatts")
_AgentPethOutputPower_Type = Gauge32
_AgentPethOutputPower_Object = MibTableColumn
agentPethOutputPower = _AgentPethOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 1, 1, 2),
    _AgentPethOutputPower_Type()
)
agentPethOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPethOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    agentPethOutputPower.setUnits("Milliwatts")
_AgentPethOutputCurrent_Type = Gauge32
_AgentPethOutputCurrent_Object = MibTableColumn
agentPethOutputCurrent = _AgentPethOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 1, 1, 3),
    _AgentPethOutputCurrent_Type()
)
agentPethOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPethOutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    agentPethOutputCurrent.setUnits("Milliamps")
_AgentPethOutputVolts_Type = Gauge32
_AgentPethOutputVolts_Object = MibTableColumn
agentPethOutputVolts = _AgentPethOutputVolts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 1, 1, 4),
    _AgentPethOutputVolts_Type()
)
agentPethOutputVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPethOutputVolts.setStatus("current")
if mibBuilder.loadTexts:
    agentPethOutputVolts.setUnits("Volts")
_AgentPethTemperature_Type = Gauge32
_AgentPethTemperature_Object = MibTableColumn
agentPethTemperature = _AgentPethTemperature_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 1, 1, 5),
    _AgentPethTemperature_Type()
)
agentPethTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPethTemperature.setStatus("current")
if mibBuilder.loadTexts:
    agentPethTemperature.setUnits("DEGREES")


class _AgentPethPowerLimitType_Type(Integer32):
    """Custom type agentPethPowerLimitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot3af", 1),
          ("user", 2))
    )


_AgentPethPowerLimitType_Type.__name__ = "Integer32"
_AgentPethPowerLimitType_Object = MibTableColumn
agentPethPowerLimitType = _AgentPethPowerLimitType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 1, 1, 6),
    _AgentPethPowerLimitType_Type()
)
agentPethPowerLimitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPethPowerLimitType.setStatus("current")
_AgentPethHighPowerEnable_Type = TruthValue
_AgentPethHighPowerEnable_Object = MibTableColumn
agentPethHighPowerEnable = _AgentPethHighPowerEnable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 1, 1, 7),
    _AgentPethHighPowerEnable_Type()
)
agentPethHighPowerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPethHighPowerEnable.setStatus("current")


class _AgentPethPowerDetectionType_Type(Integer32):
    """Custom type agentPethPowerDetectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("legacy", 1),
          ("fourPtdot3afonly", 2),
          ("fourPtdot3afandlegacy", 3),
          ("twoPtdot3afonly", 4),
          ("twoPtdot3afandlegacy", 5))
    )


_AgentPethPowerDetectionType_Type.__name__ = "Integer32"
_AgentPethPowerDetectionType_Object = MibTableColumn
agentPethPowerDetectionType = _AgentPethPowerDetectionType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 1, 1, 8),
    _AgentPethPowerDetectionType_Type()
)
agentPethPowerDetectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPethPowerDetectionType.setStatus("current")


class _AgentPethFaultStatus_Type(Integer32):
    """Custom type agentPethFaultStatus based on Integer32"""
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
        *(("none", 0),
          ("mpsAbsent", 1),
          ("short", 2),
          ("overload", 3),
          ("powerDenied", 4))
    )


_AgentPethFaultStatus_Type.__name__ = "Integer32"
_AgentPethFaultStatus_Object = MibTableColumn
agentPethFaultStatus = _AgentPethFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 1, 1, 9),
    _AgentPethFaultStatus_Type()
)
agentPethFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPethFaultStatus.setStatus("current")


class _AgentPethPortReset_Type(Integer32):
    """Custom type agentPethPortReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reset", 1))
    )


_AgentPethPortReset_Type.__name__ = "Integer32"
_AgentPethPortReset_Object = MibTableColumn
agentPethPortReset = _AgentPethPortReset_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 1, 1, 10),
    _AgentPethPortReset_Type()
)
agentPethPortReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPethPortReset.setStatus("current")
_AgentPethMainPseObjects_ObjectIdentity = ObjectIdentity
agentPethMainPseObjects = _AgentPethMainPseObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 2)
)
_AgentPethMainPseTable_Object = MibTable
agentPethMainPseTable = _AgentPethMainPseTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 2, 1)
)
if mibBuilder.loadTexts:
    agentPethMainPseTable.setStatus("current")
_AgentPethMainPseEntry_Object = MibTableRow
agentPethMainPseEntry = _AgentPethMainPseEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    agentPethMainPseEntry.setStatus("current")
_AgentPethMainPseLegacy_Type = TruthValue
_AgentPethMainPseLegacy_Object = MibTableColumn
agentPethMainPseLegacy = _AgentPethMainPseLegacy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 2, 1, 1, 1),
    _AgentPethMainPseLegacy_Type()
)
agentPethMainPseLegacy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPethMainPseLegacy.setStatus("current")
_AgentPethPseTable_Object = MibTable
agentPethPseTable = _AgentPethPseTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 3)
)
if mibBuilder.loadTexts:
    agentPethPseTable.setStatus("current")
_AgentPethPseEntry_Object = MibTableRow
agentPethPseEntry = _AgentPethPseEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 3, 1)
)
if mibBuilder.loadTexts:
    agentPethPseEntry.setStatus("current")


class _AgentPethPsePowerManagementMode_Type(Integer32):
    """Custom type agentPethPsePowerManagementMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("dynamic", 1),
          ("static", 2))
    )


_AgentPethPsePowerManagementMode_Type.__name__ = "Integer32"
_AgentPethPsePowerManagementMode_Object = MibTableColumn
agentPethPsePowerManagementMode = _AgentPethPsePowerManagementMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 3, 1, 1),
    _AgentPethPsePowerManagementMode_Type()
)
agentPethPsePowerManagementMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPethPsePowerManagementMode.setStatus("current")
_AgentPethPseAutoResetEnable_Type = TruthValue
_AgentPethPseAutoResetEnable_Object = MibTableColumn
agentPethPseAutoResetEnable = _AgentPethPseAutoResetEnable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 3, 1, 2),
    _AgentPethPseAutoResetEnable_Type()
)
agentPethPseAutoResetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPethPseAutoResetEnable.setStatus("current")
pethPsePortEntry.registerAugmentions(
    ("BROADCOM-POWER-ETHERNET-MIB",
     "agentPethPsePortEntry")
)
agentPethPsePortEntry.setIndexNames(*pethPsePortEntry.getIndexNames())
pethMainPseEntry.registerAugmentions(
    ("BROADCOM-POWER-ETHERNET-MIB",
     "agentPethMainPseEntry")
)
agentPethMainPseEntry.setIndexNames(*pethMainPseEntry.getIndexNames())
pethMainPseEntry.registerAugmentions(
    ("BROADCOM-POWER-ETHERNET-MIB",
     "agentPethPseEntry")
)
agentPethPseEntry.setIndexNames(*pethMainPseEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BROADCOM-POWER-ETHERNET-MIB",
    **{"fastPathpowerEthernetMIB": fastPathpowerEthernetMIB,
       "agentPethObjects": agentPethObjects,
       "agentPethPsePortTable": agentPethPsePortTable,
       "agentPethPsePortEntry": agentPethPsePortEntry,
       "agentPethPowerLimit": agentPethPowerLimit,
       "agentPethOutputPower": agentPethOutputPower,
       "agentPethOutputCurrent": agentPethOutputCurrent,
       "agentPethOutputVolts": agentPethOutputVolts,
       "agentPethTemperature": agentPethTemperature,
       "agentPethPowerLimitType": agentPethPowerLimitType,
       "agentPethHighPowerEnable": agentPethHighPowerEnable,
       "agentPethPowerDetectionType": agentPethPowerDetectionType,
       "agentPethFaultStatus": agentPethFaultStatus,
       "agentPethPortReset": agentPethPortReset,
       "agentPethMainPseObjects": agentPethMainPseObjects,
       "agentPethMainPseTable": agentPethMainPseTable,
       "agentPethMainPseEntry": agentPethMainPseEntry,
       "agentPethMainPseLegacy": agentPethMainPseLegacy,
       "agentPethPseTable": agentPethPseTable,
       "agentPethPseEntry": agentPethPseEntry,
       "agentPethPsePowerManagementMode": agentPethPsePowerManagementMode,
       "agentPethPseAutoResetEnable": agentPethPseAutoResetEnable}
)
