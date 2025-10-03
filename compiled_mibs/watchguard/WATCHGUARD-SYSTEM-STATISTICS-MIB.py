# SNMP MIB module (WATCHGUARD-SYSTEM-STATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\watchguard\WATCHGUARD-SYSTEM-STATISTICS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:57 2025
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

(watchguard,) = mibBuilder.importSymbols(
    "WATCHGUARD-SMI",
    "watchguard")


# MODULE-IDENTITY

wgInfoModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 6)
)
if mibBuilder.loadTexts:
    wgInfoModule.setRevisions(
        ("2007-01-25 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WgSystemStatisticsMIB_ObjectIdentity = ObjectIdentity
wgSystemStatisticsMIB = _WgSystemStatisticsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 6, 3)
)
if mibBuilder.loadTexts:
    wgSystemStatisticsMIB.setStatus("current")


class _WgSoftwareVersion_Type(OctetString):
    """Custom type wgSoftwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WgSoftwareVersion_Type.__name__ = "OctetString"
_WgSoftwareVersion_Object = MibScalar
wgSoftwareVersion = _WgSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 3, 1),
    _WgSoftwareVersion_Type()
)
wgSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgSoftwareVersion.setStatus("current")
_WgSystemCpuUtil_Type = Counter64
_WgSystemCpuUtil_Object = MibScalar
wgSystemCpuUtil = _WgSystemCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 3, 4),
    _WgSystemCpuUtil_Type()
)
wgSystemCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgSystemCpuUtil.setStatus("current")
_WgSystemTotalSendBytes_Type = Counter64
_WgSystemTotalSendBytes_Object = MibScalar
wgSystemTotalSendBytes = _WgSystemTotalSendBytes_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 3, 8),
    _WgSystemTotalSendBytes_Type()
)
wgSystemTotalSendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgSystemTotalSendBytes.setStatus("current")
_WgSystemTotalRecvBytes_Type = Counter64
_WgSystemTotalRecvBytes_Object = MibScalar
wgSystemTotalRecvBytes = _WgSystemTotalRecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 3, 9),
    _WgSystemTotalRecvBytes_Type()
)
wgSystemTotalRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgSystemTotalRecvBytes.setStatus("current")
_WgSystemTotalSendPackets_Type = Counter64
_WgSystemTotalSendPackets_Object = MibScalar
wgSystemTotalSendPackets = _WgSystemTotalSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 3, 10),
    _WgSystemTotalSendPackets_Type()
)
wgSystemTotalSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgSystemTotalSendPackets.setStatus("current")
_WgSystemTotalRecvPackets_Type = Counter64
_WgSystemTotalRecvPackets_Object = MibScalar
wgSystemTotalRecvPackets = _WgSystemTotalRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 3, 11),
    _WgSystemTotalRecvPackets_Type()
)
wgSystemTotalRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgSystemTotalRecvPackets.setStatus("current")
_WgSystemStreamReqTotal_Type = Counter64
_WgSystemStreamReqTotal_Object = MibScalar
wgSystemStreamReqTotal = _WgSystemStreamReqTotal_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 3, 30),
    _WgSystemStreamReqTotal_Type()
)
wgSystemStreamReqTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgSystemStreamReqTotal.setStatus("current")
_WgSystemStreamReqDrop_Type = Counter64
_WgSystemStreamReqDrop_Object = MibScalar
wgSystemStreamReqDrop = _WgSystemStreamReqDrop_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 3, 34),
    _WgSystemStreamReqDrop_Type()
)
wgSystemStreamReqDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgSystemStreamReqDrop.setStatus("current")
_WgSystemCpuUtil1_Type = Counter64
_WgSystemCpuUtil1_Object = MibScalar
wgSystemCpuUtil1 = _WgSystemCpuUtil1_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 3, 77),
    _WgSystemCpuUtil1_Type()
)
wgSystemCpuUtil1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgSystemCpuUtil1.setStatus("current")
_WgSystemCpuUtil5_Type = Counter64
_WgSystemCpuUtil5_Object = MibScalar
wgSystemCpuUtil5 = _WgSystemCpuUtil5_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 3, 78),
    _WgSystemCpuUtil5_Type()
)
wgSystemCpuUtil5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgSystemCpuUtil5.setStatus("current")
_WgSystemCpuUtil15_Type = Counter64
_WgSystemCpuUtil15_Object = MibScalar
wgSystemCpuUtil15 = _WgSystemCpuUtil15_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 3, 79),
    _WgSystemCpuUtil15_Type()
)
wgSystemCpuUtil15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgSystemCpuUtil15.setStatus("current")
_WgSystemCurrActiveConns_Type = Counter64
_WgSystemCurrActiveConns_Object = MibScalar
wgSystemCurrActiveConns = _WgSystemCurrActiveConns_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 3, 80),
    _WgSystemCurrActiveConns_Type()
)
wgSystemCurrActiveConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgSystemCurrActiveConns.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WATCHGUARD-SYSTEM-STATISTICS-MIB",
    **{"wgInfoModule": wgInfoModule,
       "wgSystemStatisticsMIB": wgSystemStatisticsMIB,
       "wgSoftwareVersion": wgSoftwareVersion,
       "wgSystemCpuUtil": wgSystemCpuUtil,
       "wgSystemTotalSendBytes": wgSystemTotalSendBytes,
       "wgSystemTotalRecvBytes": wgSystemTotalRecvBytes,
       "wgSystemTotalSendPackets": wgSystemTotalSendPackets,
       "wgSystemTotalRecvPackets": wgSystemTotalRecvPackets,
       "wgSystemStreamReqTotal": wgSystemStreamReqTotal,
       "wgSystemStreamReqDrop": wgSystemStreamReqDrop,
       "wgSystemCpuUtil1": wgSystemCpuUtil1,
       "wgSystemCpuUtil5": wgSystemCpuUtil5,
       "wgSystemCpuUtil15": wgSystemCpuUtil15,
       "wgSystemCurrActiveConns": wgSystemCurrActiveConns}
)
