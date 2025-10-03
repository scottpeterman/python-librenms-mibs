# SNMP MIB module (IBM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ibm\IBM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:00:43 2025
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmResearch_ObjectIdentity = ObjectIdentity
ibmResearch = _IbmResearch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 2)
)
_IbmAgents_ObjectIdentity = ObjectIdentity
ibmAgents = _IbmAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3)
)
_IbmArchitecture_ObjectIdentity = ObjectIdentity
ibmArchitecture = _IbmArchitecture_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5)
)
_Alert_ObjectIdentity = ObjectIdentity
alert = _Alert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 1)
)
_Fddi_ObjectIdentity = ObjectIdentity
fddi = _Fddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 2)
)
_Topology_ObjectIdentity = ObjectIdentity
topology = _Topology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 3)
)
_TokenRing_ObjectIdentity = ObjectIdentity
tokenRing = _TokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 4)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_Ibm3172_ObjectIdentity = ObjectIdentity
ibm3172 = _Ibm3172_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 1)
)
_Ibm6611_ObjectIdentity = ObjectIdentity
ibm6611 = _Ibm6611_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2)
)
_NetView6000_ObjectIdentity = ObjectIdentity
netView6000 = _NetView6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 3)
)
_NetView6000SubAgent_ObjectIdentity = ObjectIdentity
netView6000SubAgent = _NetView6000SubAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 4)
)
_SystemsMonitor6000_ObjectIdentity = ObjectIdentity
systemsMonitor6000 = _SystemsMonitor6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBM-MIB",
    **{"ibm": ibm,
       "ibmResearch": ibmResearch,
       "ibmAgents": ibmAgents,
       "ibmArchitecture": ibmArchitecture,
       "alert": alert,
       "fddi": fddi,
       "topology": topology,
       "tokenRing": tokenRing,
       "ibmProd": ibmProd,
       "ibm3172": ibm3172,
       "ibm6611": ibm6611,
       "netView6000": netView6000,
       "netView6000SubAgent": netView6000SubAgent,
       "systemsMonitor6000": systemsMonitor6000}
)
