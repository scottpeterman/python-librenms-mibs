# SNMP MIB module (DCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\smartoptics\DCP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:28:19 2025
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

(smartoptics,) = mibBuilder.importSymbols(
    "SO-MIB",
    "smartoptics")


# MODULE-IDENTITY

dcpGlobalModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dcpGlobalModule.setRevisions(
        ("2018-10-08 14:44",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dcp_ObjectIdentity = ObjectIdentity
dcp = _Dcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2)
)
if mibBuilder.loadTexts:
    dcp.setStatus("current")
_DcpReg_ObjectIdentity = ObjectIdentity
dcpReg = _DcpReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 1)
)
if mibBuilder.loadTexts:
    dcpReg.setStatus("current")
_DcpModules_ObjectIdentity = ObjectIdentity
dcpModules = _DcpModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dcpModules.setStatus("current")
_DcpGeneric_ObjectIdentity = ObjectIdentity
dcpGeneric = _DcpGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2)
)
if mibBuilder.loadTexts:
    dcpGeneric.setStatus("current")
_DcpProducts_ObjectIdentity = ObjectIdentity
dcpProducts = _DcpProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 3)
)
if mibBuilder.loadTexts:
    dcpProducts.setStatus("current")
_DcpCaps_ObjectIdentity = ObjectIdentity
dcpCaps = _DcpCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 4)
)
if mibBuilder.loadTexts:
    dcpCaps.setStatus("current")
_DcpReqs_ObjectIdentity = ObjectIdentity
dcpReqs = _DcpReqs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 5)
)
if mibBuilder.loadTexts:
    dcpReqs.setStatus("current")
_DcpExpr_ObjectIdentity = ObjectIdentity
dcpExpr = _DcpExpr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 6)
)
if mibBuilder.loadTexts:
    dcpExpr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DCP-MIB",
    **{"dcp": dcp,
       "dcpReg": dcpReg,
       "dcpModules": dcpModules,
       "dcpGlobalModule": dcpGlobalModule,
       "dcpGeneric": dcpGeneric,
       "dcpProducts": dcpProducts,
       "dcpCaps": dcpCaps,
       "dcpReqs": dcpReqs,
       "dcpExpr": dcpExpr}
)
