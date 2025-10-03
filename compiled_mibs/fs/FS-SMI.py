# SNMP MIB module (FS-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fs\FS-SMI
# Produced by pysmi-1.6.2 at Thu Oct  2 11:45:46 2025
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
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10)
)
if mibBuilder.loadTexts:
    switchMib.setRevisions(
        ("2002-03-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fs_ObjectIdentity = ObjectIdentity
fs = _Fs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1)
)
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1)
)
_FsSwitchProducts_ObjectIdentity = ObjectIdentity
fsSwitchProducts = _FsSwitchProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    fsSwitchProducts.setStatus("current")
_FsMgmt_ObjectIdentity = ObjectIdentity
fsMgmt = _FsMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2)
)
if mibBuilder.loadTexts:
    fsMgmt.setStatus("current")
_FsAgentCapability_ObjectIdentity = ObjectIdentity
fsAgentCapability = _FsAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 3)
)
if mibBuilder.loadTexts:
    fsAgentCapability.setStatus("current")
_FsModules_ObjectIdentity = ObjectIdentity
fsModules = _FsModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 4)
)
if mibBuilder.loadTexts:
    fsModules.setStatus("current")
_FsExperiment_ObjectIdentity = ObjectIdentity
fsExperiment = _FsExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 5)
)
if mibBuilder.loadTexts:
    fsExperiment.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-SMI",
    **{"fs": fs,
       "products": products,
       "switch": switch,
       "switchMib": switchMib,
       "fsSwitchProducts": fsSwitchProducts,
       "fsMgmt": fsMgmt,
       "fsAgentCapability": fsAgentCapability,
       "fsModules": fsModules,
       "fsExperiment": fsExperiment}
)
