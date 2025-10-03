# SNMP MIB module (DASAN-GFAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\DASAN-GFAST-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:05 2025
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

(dasanEvents,
 dasanMgmt) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "dasanEvents",
    "dasanMgmt")

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

gFastMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 102)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GFastTestObj1_ObjectIdentity = ObjectIdentity
gFastTestObj1 = _GFastTestObj1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 102, 1)
)
_GFastTestObj1Temp1_ObjectIdentity = ObjectIdentity
gFastTestObj1Temp1 = _GFastTestObj1Temp1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 102, 1, 1)
)
_GFastTestObj1Temp2_ObjectIdentity = ObjectIdentity
gFastTestObj1Temp2 = _GFastTestObj1Temp2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 102, 1, 2)
)
_GFastTestObj2_ObjectIdentity = ObjectIdentity
gFastTestObj2 = _GFastTestObj2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 102, 2)
)
_GFastTestObj2Temp1_ObjectIdentity = ObjectIdentity
gFastTestObj2Temp1 = _GFastTestObj2Temp1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 102, 2, 1)
)
_GFastTestObj2Temp1Val1_Type = Integer32
_GFastTestObj2Temp1Val1_Object = MibScalar
gFastTestObj2Temp1Val1 = _GFastTestObj2Temp1Val1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 102, 2, 1, 1),
    _GFastTestObj2Temp1Val1_Type()
)
gFastTestObj2Temp1Val1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gFastTestObj2Temp1Val1.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DASAN-GFAST-MIB",
    **{"gFastMIB": gFastMIB,
       "gFastTestObj1": gFastTestObj1,
       "gFastTestObj1Temp1": gFastTestObj1Temp1,
       "gFastTestObj1Temp2": gFastTestObj1Temp2,
       "gFastTestObj2": gFastTestObj2,
       "gFastTestObj2Temp1": gFastTestObj2Temp1,
       "gFastTestObj2Temp1Val1": gFastTestObj2Temp1Val1}
)
