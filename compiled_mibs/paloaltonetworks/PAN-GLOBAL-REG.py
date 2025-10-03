# SNMP MIB module (PAN-GLOBAL-REG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\paloaltonetworks\PAN-GLOBAL-REG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:16 2025
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

panGlobalRegModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 1)
)
if mibBuilder.loadTexts:
    panGlobalRegModule.setRevisions(
        ("2011-02-09 16:10",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PanRoot_ObjectIdentity = ObjectIdentity
panRoot = _PanRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461)
)
if mibBuilder.loadTexts:
    panRoot.setStatus("current")
_PanReg_ObjectIdentity = ObjectIdentity
panReg = _PanReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 1)
)
if mibBuilder.loadTexts:
    panReg.setStatus("current")
_PanModules_ObjectIdentity = ObjectIdentity
panModules = _PanModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1)
)
if mibBuilder.loadTexts:
    panModules.setStatus("current")
_PanMibs_ObjectIdentity = ObjectIdentity
panMibs = _PanMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2)
)
if mibBuilder.loadTexts:
    panMibs.setStatus("current")
_PanCommonMib_ObjectIdentity = ObjectIdentity
panCommonMib = _PanCommonMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1)
)
if mibBuilder.loadTexts:
    panCommonMib.setStatus("current")
_PanSpecificMib_ObjectIdentity = ObjectIdentity
panSpecificMib = _PanSpecificMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 2)
)
if mibBuilder.loadTexts:
    panSpecificMib.setStatus("current")
_PanProductsMibs_ObjectIdentity = ObjectIdentity
panProductsMibs = _PanProductsMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3)
)
if mibBuilder.loadTexts:
    panProductsMibs.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PAN-GLOBAL-REG",
    **{"panRoot": panRoot,
       "panReg": panReg,
       "panModules": panModules,
       "panGlobalRegModule": panGlobalRegModule,
       "panMibs": panMibs,
       "panCommonMib": panCommonMib,
       "panSpecificMib": panSpecificMib,
       "panProductsMibs": panProductsMibs}
)
