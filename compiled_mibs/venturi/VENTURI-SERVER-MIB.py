# SNMP MIB module (VENTURI-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\venturi\VENTURI-SERVER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:48 2025
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

(venturiMgmt,
 venturiProducts) = mibBuilder.importSymbols(
    "VENTURI-WIRELESS-SMI",
    "venturiMgmt",
    "venturiProducts")


# MODULE-IDENTITY

vServerMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1)
)
if mibBuilder.loadTexts:
    vServerMgmt.setRevisions(
        ("2011-01-03 00:00",
         "2010-01-06 00:00",
         "2008-06-03 00:00",
         "2008-05-06 00:00",
         "2008-04-08 00:00",
         "2005-02-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VenturiServer_ObjectIdentity = ObjectIdentity
venturiServer = _VenturiServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 11, 1)
)
if mibBuilder.loadTexts:
    venturiServer.setStatus("current")
_Venturi3000_ObjectIdentity = ObjectIdentity
venturi3000 = _Venturi3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 11, 1, 1)
)
_Venturi20_ObjectIdentity = ObjectIdentity
venturi20 = _Venturi20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 11, 1, 2)
)
_Venturi100e_ObjectIdentity = ObjectIdentity
venturi100e = _Venturi100e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 11, 1, 3)
)
_VenturiSP_ObjectIdentity = ObjectIdentity
venturiSP = _VenturiSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 11, 1, 4)
)
_Venturi5000_ObjectIdentity = ObjectIdentity
venturi5000 = _Venturi5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 11, 1, 5)
)
_VBlade1000_ObjectIdentity = ObjectIdentity
vBlade1000 = _VBlade1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 11, 1, 6)
)
_Venturi5220_ObjectIdentity = ObjectIdentity
venturi5220 = _Venturi5220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 11, 1, 7)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VENTURI-SERVER-MIB",
    **{"venturiServer": venturiServer,
       "venturi3000": venturi3000,
       "venturi20": venturi20,
       "venturi100e": venturi100e,
       "venturiSP": venturiSP,
       "venturi5000": venturi5000,
       "vBlade1000": vBlade1000,
       "venturi5220": venturi5220,
       "vServerMgmt": vServerMgmt}
)
