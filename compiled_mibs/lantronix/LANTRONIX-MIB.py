# SNMP MIB module (LANTRONIX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\lantronix\LANTRONIX-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:08:21 2025
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

lantronix = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 244)
)
if mibBuilder.loadTexts:
    lantronix.setRevisions(
        ("2007-03-01 00:00",
         "2006-11-10 00:00",
         "2004-12-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1)
)
_Slc_ObjectIdentity = ObjectIdentity
slc = _Slc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1)
)
_Slk_ObjectIdentity = ObjectIdentity
slk = _Slk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 8)
)
_Slp_ObjectIdentity = ObjectIdentity
slp = _Slp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 9)
)
_Slm_ObjectIdentity = ObjectIdentity
slm = _Slm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 10)
)
_Sls_ObjectIdentity = ObjectIdentity
sls = _Sls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 11)
)
_Ltxlna_ObjectIdentity = ObjectIdentity
ltxlna = _Ltxlna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 10)
)
_Ltxlrp_ObjectIdentity = ObjectIdentity
ltxlrp = _Ltxlrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 11)
)
_Ltxlsw_ObjectIdentity = ObjectIdentity
ltxlsw = _Ltxlsw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 12)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANTRONIX-MIB",
    **{"lantronix": lantronix,
       "products": products,
       "slc": slc,
       "slk": slk,
       "slp": slp,
       "slm": slm,
       "sls": sls,
       "ltxlna": ltxlna,
       "ltxlrp": ltxlrp,
       "ltxlsw": ltxlsw}
)
