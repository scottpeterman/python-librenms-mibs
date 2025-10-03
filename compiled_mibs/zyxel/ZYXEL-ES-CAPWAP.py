# SNMP MIB module (ZYXEL-ES-CAPWAP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\zyxel\ZYXEL-ES-CAPWAP
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:54 2025
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
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

esCAPWAP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CapwapInfo_ObjectIdentity = ObjectIdentity
capwapInfo = _CapwapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 1)
)
if mibBuilder.loadTexts:
    capwapInfo.setStatus("current")
_CapwapOnlineAP_Type = Unsigned32
_CapwapOnlineAP_Object = MibScalar
capwapOnlineAP = _CapwapOnlineAP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 1, 1),
    _CapwapOnlineAP_Type()
)
capwapOnlineAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapOnlineAP.setStatus("current")
_CapwapOfflineAP_Type = Unsigned32
_CapwapOfflineAP_Object = MibScalar
capwapOfflineAP = _CapwapOfflineAP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 1, 2),
    _CapwapOfflineAP_Type()
)
capwapOfflineAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapOfflineAP.setStatus("current")
_CapwapUnMgntAP_Type = Unsigned32
_CapwapUnMgntAP_Object = MibScalar
capwapUnMgntAP = _CapwapUnMgntAP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 1, 3),
    _CapwapUnMgntAP_Type()
)
capwapUnMgntAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapUnMgntAP.setStatus("current")
_CapwapTotalStation_Type = Unsigned32
_CapwapTotalStation_Object = MibScalar
capwapTotalStation = _CapwapTotalStation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 1, 4),
    _CapwapTotalStation_Type()
)
capwapTotalStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapTotalStation.setStatus("current")
_CapwapTraps_ObjectIdentity = ObjectIdentity
capwapTraps = _CapwapTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 2)
)
if mibBuilder.loadTexts:
    capwapTraps.setStatus("current")


class _CapwapTrapsControl_Type(Integer32):
    """Custom type capwapTrapsControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_CapwapTrapsControl_Type.__name__ = "Integer32"
_CapwapTrapsControl_Object = MibScalar
capwapTrapsControl = _CapwapTrapsControl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 2, 1),
    _CapwapTrapsControl_Type()
)
capwapTrapsControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapTrapsControl.setStatus("current")
_CapwapTrapsItems_ObjectIdentity = ObjectIdentity
capwapTrapsItems = _CapwapTrapsItems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 2, 2)
)
if mibBuilder.loadTexts:
    capwapTrapsItems.setStatus("current")

# Managed Objects groups


# Notification objects

capwapWTPOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    capwapWTPOnline.setStatus(
        "current"
    )

capwapWTPOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    capwapWTPOffline.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-ES-CAPWAP",
    **{"esCAPWAP": esCAPWAP,
       "capwapInfo": capwapInfo,
       "capwapOnlineAP": capwapOnlineAP,
       "capwapOfflineAP": capwapOfflineAP,
       "capwapUnMgntAP": capwapUnMgntAP,
       "capwapTotalStation": capwapTotalStation,
       "capwapTraps": capwapTraps,
       "capwapTrapsControl": capwapTrapsControl,
       "capwapTrapsItems": capwapTrapsItems,
       "capwapWTPOnline": capwapWTPOnline,
       "capwapWTPOffline": capwapWTPOffline}
)
