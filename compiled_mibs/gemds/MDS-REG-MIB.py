# SNMP MIB module (MDS-REG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\gemds\MDS-REG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:47:20 2025
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

mdsGlobalRegModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 4)
)
if mibBuilder.loadTexts:
    mdsGlobalRegModule.setRevisions(
        ("2006-02-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MdsRoot_ObjectIdentity = ObjectIdentity
mdsRoot = _MdsRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130)
)
if mibBuilder.loadTexts:
    mdsRoot.setStatus("current")
_MdsWideband_ObjectIdentity = ObjectIdentity
mdsWideband = _MdsWideband_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 1)
)
if mibBuilder.loadTexts:
    mdsWideband.setStatus("current")
_MdsPointToPoint_ObjectIdentity = ObjectIdentity
mdsPointToPoint = _MdsPointToPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 1, 1)
)
if mibBuilder.loadTexts:
    mdsPointToPoint.setStatus("current")
_MdsNarrowband_ObjectIdentity = ObjectIdentity
mdsNarrowband = _MdsNarrowband_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 2)
)
if mibBuilder.loadTexts:
    mdsNarrowband.setStatus("current")
_MdsPointToMultiPoint_ObjectIdentity = ObjectIdentity
mdsPointToMultiPoint = _MdsPointToMultiPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 2, 1)
)
if mibBuilder.loadTexts:
    mdsPointToMultiPoint.setStatus("current")
_MdsBroadband_ObjectIdentity = ObjectIdentity
mdsBroadband = _MdsBroadband_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 3)
)
if mibBuilder.loadTexts:
    mdsBroadband.setStatus("current")
_MdsSoftware_ObjectIdentity = ObjectIdentity
mdsSoftware = _MdsSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 9)
)
if mibBuilder.loadTexts:
    mdsSoftware.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MDS-REG-MIB",
    **{"mdsRoot": mdsRoot,
       "mdsWideband": mdsWideband,
       "mdsPointToPoint": mdsPointToPoint,
       "mdsNarrowband": mdsNarrowband,
       "mdsPointToMultiPoint": mdsPointToMultiPoint,
       "mdsBroadband": mdsBroadband,
       "mdsGlobalRegModule": mdsGlobalRegModule,
       "mdsSoftware": mdsSoftware}
)
