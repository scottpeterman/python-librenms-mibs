# SNMP MIB module (CONEL-IO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\icr-os\CONEL-IO-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:01:12 2025
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

_Conel_ObjectIdentity = ObjectIdentity
conel = _Conel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140)
)
_Protocols_ObjectIdentity = ObjectIdentity
protocols = _Protocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 2)
)
_Io_ObjectIdentity = ObjectIdentity
io = _Io_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 2, 3)
)
_IoBin0_Type = Gauge32
_IoBin0_Object = MibScalar
ioBin0 = _IoBin0_Object(
    (1, 3, 6, 1, 4, 1, 30140, 2, 3, 1),
    _IoBin0_Type()
)
ioBin0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioBin0.setStatus("current")
_IoOut0_Type = Gauge32
_IoOut0_Object = MibScalar
ioOut0 = _IoOut0_Object(
    (1, 3, 6, 1, 4, 1, 30140, 2, 3, 2),
    _IoOut0_Type()
)
ioOut0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioOut0.setStatus("current")
_IoBin1_Type = Gauge32
_IoBin1_Object = MibScalar
ioBin1 = _IoBin1_Object(
    (1, 3, 6, 1, 4, 1, 30140, 2, 3, 3),
    _IoBin1_Type()
)
ioBin1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioBin1.setStatus("current")
_IoOut1_Type = Gauge32
_IoOut1_Object = MibScalar
ioOut1 = _IoOut1_Object(
    (1, 3, 6, 1, 4, 1, 30140, 2, 3, 4),
    _IoOut1_Type()
)
ioOut1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioOut1.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CONEL-IO-MIB",
    **{"conel": conel,
       "protocols": protocols,
       "io": io,
       "ioBin0": ioBin0,
       "ioOut0": ioOut0,
       "ioBin1": ioBin1,
       "ioOut1": ioOut1}
)
