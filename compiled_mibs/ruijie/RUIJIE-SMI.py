# SNMP MIB module (RUIJIE-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ruijie\RUIJIE-SMI
# Produced by pysmi-1.6.2 at Thu Oct  2 12:24:14 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

switchMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10)
)
if mibBuilder.loadTexts:
    switchMib.setRevisions(
        ("2002-03-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ruijie_ObjectIdentity = ObjectIdentity
ruijie = _Ruijie_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1)
)
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1)
)
_RuijieSwitchProducts_ObjectIdentity = ObjectIdentity
ruijieSwitchProducts = _RuijieSwitchProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    ruijieSwitchProducts.setStatus("current")
_RuijieMgmt_ObjectIdentity = ObjectIdentity
ruijieMgmt = _RuijieMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2)
)
if mibBuilder.loadTexts:
    ruijieMgmt.setStatus("current")
_RuijieAgentCapability_ObjectIdentity = ObjectIdentity
ruijieAgentCapability = _RuijieAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 3)
)
if mibBuilder.loadTexts:
    ruijieAgentCapability.setStatus("current")
_RuijieModules_ObjectIdentity = ObjectIdentity
ruijieModules = _RuijieModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 4)
)
if mibBuilder.loadTexts:
    ruijieModules.setStatus("current")
_RuijieExperiment_ObjectIdentity = ObjectIdentity
ruijieExperiment = _RuijieExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 5)
)
if mibBuilder.loadTexts:
    ruijieExperiment.setStatus("current")
_SoftPlatform_ObjectIdentity = ObjectIdentity
softPlatform = _SoftPlatform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 2)
)
_Sonic_ObjectIdentity = ObjectIdentity
sonic = _Sonic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 2, 1)
)
_RuijieStandard_ObjectIdentity = ObjectIdentity
ruijieStandard = _RuijieStandard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 3507)
)
_RuijieSystem_ObjectIdentity = ObjectIdentity
ruijieSystem = _RuijieSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 3507, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-SMI",
    **{"ruijie": ruijie,
       "products": products,
       "switch": switch,
       "switchMib": switchMib,
       "ruijieSwitchProducts": ruijieSwitchProducts,
       "ruijieMgmt": ruijieMgmt,
       "ruijieAgentCapability": ruijieAgentCapability,
       "ruijieModules": ruijieModules,
       "ruijieExperiment": ruijieExperiment,
       "softPlatform": softPlatform,
       "sonic": sonic,
       "ruijieStandard": ruijieStandard,
       "ruijieSystem": ruijieSystem}
)
