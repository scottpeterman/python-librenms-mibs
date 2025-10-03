# SNMP MIB module (AT-SMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\allied\AT-SMI-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:20:20 2025
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

alliedTelesis = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207)
)
if mibBuilder.loadTexts:
    alliedTelesis.setRevisions(
        ("2014-09-30 00:00",
         "2010-06-15 00:15",
         "2008-02-28 00:00",
         "2006-06-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DisplayStringUnsized(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"


# MIB Managed Objects in the order of their OIDs

_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1)
)
if mibBuilder.loadTexts:
    products.setStatus("current")
_Wirelesslan_ObjectIdentity = ObjectIdentity
wirelesslan = _Wirelesslan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 13)
)
if mibBuilder.loadTexts:
    wirelesslan.setStatus("current")
_MibObject_ObjectIdentity = ObjectIdentity
mibObject = _MibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8)
)
if mibBuilder.loadTexts:
    mibObject.setStatus("current")
_BrouterMib_ObjectIdentity = ObjectIdentity
brouterMib = _BrouterMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4)
)
if mibBuilder.loadTexts:
    brouterMib.setStatus("current")
_AtRouter_ObjectIdentity = ObjectIdentity
atRouter = _AtRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4)
)
if mibBuilder.loadTexts:
    atRouter.setStatus("current")
_Objects_ObjectIdentity = ObjectIdentity
objects = _Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1)
)
if mibBuilder.loadTexts:
    objects.setStatus("current")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 2)
)
if mibBuilder.loadTexts:
    traps.setStatus("current")
_Sysinfo_ObjectIdentity = ObjectIdentity
sysinfo = _Sysinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3)
)
if mibBuilder.loadTexts:
    sysinfo.setStatus("current")
_Modules_ObjectIdentity = ObjectIdentity
modules = _Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4)
)
if mibBuilder.loadTexts:
    modules.setStatus("current")
_ArInterfaces_ObjectIdentity = ObjectIdentity
arInterfaces = _ArInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5)
)
if mibBuilder.loadTexts:
    arInterfaces.setStatus("current")
_Protocols_ObjectIdentity = ObjectIdentity
protocols = _Protocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 6)
)
if mibBuilder.loadTexts:
    protocols.setStatus("current")
_AtAgents_ObjectIdentity = ObjectIdentity
atAgents = _AtAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 7)
)
if mibBuilder.loadTexts:
    atAgents.setStatus("current")
_WirelessLanmMIB_ObjectIdentity = ObjectIdentity
wirelessLanmMIB = _WirelessLanmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42)
)
if mibBuilder.loadTexts:
    wirelessLanmMIB.setStatus("current")
_AtUWC_ObjectIdentity = ObjectIdentity
atUWC = _AtUWC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8)
)
if mibBuilder.loadTexts:
    atUWC.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-SMI-MIB",
    **{"DisplayStringUnsized": DisplayStringUnsized,
       "alliedTelesis": alliedTelesis,
       "products": products,
       "wirelesslan": wirelesslan,
       "mibObject": mibObject,
       "brouterMib": brouterMib,
       "atRouter": atRouter,
       "objects": objects,
       "traps": traps,
       "sysinfo": sysinfo,
       "modules": modules,
       "arInterfaces": arInterfaces,
       "protocols": protocols,
       "atAgents": atAgents,
       "wirelessLanmMIB": wirelessLanmMIB,
       "atUWC": atUWC}
)
