# SNMP MIB module (BDCOM-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bdcom\BDCOM-SMI
# Produced by pysmi-1.6.2 at Thu Oct  2 11:45:25 2025
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

bdcom = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3320)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BdcomProducts_ObjectIdentity = ObjectIdentity
bdcomProducts = _BdcomProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 1)
)
if mibBuilder.loadTexts:
    bdcomProducts.setStatus("current")
_Bdlocal_ObjectIdentity = ObjectIdentity
bdlocal = _Bdlocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 2)
)
if mibBuilder.loadTexts:
    bdlocal.setStatus("current")
_Bdtemporary_ObjectIdentity = ObjectIdentity
bdtemporary = _Bdtemporary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 3)
)
if mibBuilder.loadTexts:
    bdtemporary.setStatus("current")
_BdMgmt_ObjectIdentity = ObjectIdentity
bdMgmt = _BdMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9)
)
if mibBuilder.loadTexts:
    bdMgmt.setStatus("current")
_BdcomModules_ObjectIdentity = ObjectIdentity
bdcomModules = _BdcomModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 12)
)
if mibBuilder.loadTexts:
    bdcomModules.setStatus("current")
_BdcomPolicyAuto_ObjectIdentity = ObjectIdentity
bdcomPolicyAuto = _BdcomPolicyAuto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 18)
)
if mibBuilder.loadTexts:
    bdcomPolicyAuto.setStatus("current")
_BdcomPibToMib_ObjectIdentity = ObjectIdentity
bdcomPibToMib = _BdcomPibToMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2)
)
if mibBuilder.loadTexts:
    bdcomPibToMib.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BDCOM-SMI",
    **{"bdcom": bdcom,
       "bdcomProducts": bdcomProducts,
       "bdlocal": bdlocal,
       "bdtemporary": bdtemporary,
       "bdMgmt": bdMgmt,
       "bdcomModules": bdcomModules,
       "bdcomPolicyAuto": bdcomPolicyAuto,
       "bdcomPibToMib": bdcomPibToMib}
)
