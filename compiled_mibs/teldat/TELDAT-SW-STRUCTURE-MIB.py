# SNMP MIB module (TELDAT-SW-STRUCTURE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\teldat\TELDAT-SW-STRUCTURE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:57 2025
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

(telproducts,) = mibBuilder.importSymbols(
    "TELDAT-MIB",
    "telproducts")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TelProductsNucleox_ObjectIdentity = ObjectIdentity
telProductsNucleox = _TelProductsNucleox_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1)
)
_TelProductsNpConfig_ObjectIdentity = ObjectIdentity
telProductsNpConfig = _TelProductsNpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 1)
)
_TelProdNpConfInterface_ObjectIdentity = ObjectIdentity
telProdNpConfInterface = _TelProdNpConfInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 1, 4)
)
_TelProdNpConfProtocol_ObjectIdentity = ObjectIdentity
telProdNpConfProtocol = _TelProdNpConfProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 1, 5)
)
_TelProductsNpMonit_ObjectIdentity = ObjectIdentity
telProductsNpMonit = _TelProductsNpMonit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2)
)
_TelProdNpMonitSistema_ObjectIdentity = ObjectIdentity
telProdNpMonitSistema = _TelProdNpMonitSistema_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1)
)
_TelProdNpMonInterface_ObjectIdentity = ObjectIdentity
telProdNpMonInterface = _TelProdNpMonInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2)
)
_TelProdNpMonInterfRouter_ObjectIdentity = ObjectIdentity
telProdNpMonInterfRouter = _TelProdNpMonInterfRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2)
)
_TelProdNpMonInterfNodo_ObjectIdentity = ObjectIdentity
telProdNpMonInterfNodo = _TelProdNpMonInterfNodo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 3)
)
_TelProdNpMonProtocols_ObjectIdentity = ObjectIdentity
telProdNpMonProtocols = _TelProdNpMonProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 3)
)
_TelProdNpMonProtIP_ObjectIdentity = ObjectIdentity
telProdNpMonProtIP = _TelProdNpMonProtIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 3, 1)
)
_TelProdNpMonFeatures_ObjectIdentity = ObjectIdentity
telProdNpMonFeatures = _TelProdNpMonFeatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TELDAT-SW-STRUCTURE-MIB",
    **{"telProductsNucleox": telProductsNucleox,
       "telProductsNpConfig": telProductsNpConfig,
       "telProdNpConfInterface": telProdNpConfInterface,
       "telProdNpConfProtocol": telProdNpConfProtocol,
       "telProductsNpMonit": telProductsNpMonit,
       "telProdNpMonitSistema": telProdNpMonitSistema,
       "telProdNpMonInterface": telProdNpMonInterface,
       "telProdNpMonInterfRouter": telProdNpMonInterfRouter,
       "telProdNpMonInterfNodo": telProdNpMonInterfNodo,
       "telProdNpMonProtocols": telProdNpMonProtocols,
       "telProdNpMonProtIP": telProdNpMonProtIP,
       "telProdNpMonFeatures": telProdNpMonFeatures}
)
