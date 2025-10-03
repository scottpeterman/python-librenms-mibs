# SNMP MIB module (ARRIS-C3-TFTPD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\ARRIS-C3-TFTPD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:18:09 2025
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

(cmtsC3,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "cmtsC3")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cmtsC3TFTPDMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DcxTFTPDObjects_ObjectIdentity = ObjectIdentity
dcxTFTPDObjects = _DcxTFTPDObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 9, 1)
)


class _DcxTFTPDServerState_Type(Integer32):
    """Custom type dcxTFTPDServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_DcxTFTPDServerState_Type.__name__ = "Integer32"
_DcxTFTPDServerState_Object = MibScalar
dcxTFTPDServerState = _DcxTFTPDServerState_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 9, 1, 1),
    _DcxTFTPDServerState_Type()
)
dcxTFTPDServerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxTFTPDServerState.setStatus("current")
_DcxTFTPDCurrentDirectory_Type = DisplayString
_DcxTFTPDCurrentDirectory_Object = MibScalar
dcxTFTPDCurrentDirectory = _DcxTFTPDCurrentDirectory_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 9, 1, 2),
    _DcxTFTPDCurrentDirectory_Type()
)
dcxTFTPDCurrentDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxTFTPDCurrentDirectory.setStatus("current")


class _DcxTFTPDIpVerification_Type(Integer32):
    """Custom type dcxTFTPDIpVerification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DcxTFTPDIpVerification_Type.__name__ = "Integer32"
_DcxTFTPDIpVerification_Object = MibScalar
dcxTFTPDIpVerification = _DcxTFTPDIpVerification_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 9, 1, 3),
    _DcxTFTPDIpVerification_Type()
)
dcxTFTPDIpVerification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxTFTPDIpVerification.setStatus("current")
_DcxTFTPDClearCache_Type = TruthValue
_DcxTFTPDClearCache_Object = MibScalar
dcxTFTPDClearCache = _DcxTFTPDClearCache_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 9, 1, 4),
    _DcxTFTPDClearCache_Type()
)
dcxTFTPDClearCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxTFTPDClearCache.setStatus("current")
_DcxTFTPDReadRequests_Type = Counter32
_DcxTFTPDReadRequests_Object = MibScalar
dcxTFTPDReadRequests = _DcxTFTPDReadRequests_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 9, 1, 5),
    _DcxTFTPDReadRequests_Type()
)
dcxTFTPDReadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxTFTPDReadRequests.setStatus("current")
_DcxTFTPDReadRequestsDropped_Type = Counter32
_DcxTFTPDReadRequestsDropped_Object = MibScalar
dcxTFTPDReadRequestsDropped = _DcxTFTPDReadRequestsDropped_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 9, 1, 6),
    _DcxTFTPDReadRequestsDropped_Type()
)
dcxTFTPDReadRequestsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxTFTPDReadRequestsDropped.setStatus("current")
_DcxTFTPDReadRequestsFailed_Type = Counter32
_DcxTFTPDReadRequestsFailed_Object = MibScalar
dcxTFTPDReadRequestsFailed = _DcxTFTPDReadRequestsFailed_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 9, 1, 7),
    _DcxTFTPDReadRequestsFailed_Type()
)
dcxTFTPDReadRequestsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxTFTPDReadRequestsFailed.setStatus("current")
_DcxTFTPDReadBytes_Type = Counter32
_DcxTFTPDReadBytes_Object = MibScalar
dcxTFTPDReadBytes = _DcxTFTPDReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 9, 1, 8),
    _DcxTFTPDReadBytes_Type()
)
dcxTFTPDReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxTFTPDReadBytes.setStatus("current")
_DcxTFTPDWriteRequests_Type = Counter32
_DcxTFTPDWriteRequests_Object = MibScalar
dcxTFTPDWriteRequests = _DcxTFTPDWriteRequests_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 9, 1, 9),
    _DcxTFTPDWriteRequests_Type()
)
dcxTFTPDWriteRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxTFTPDWriteRequests.setStatus("current")
_DcxTFTPDWriteRequestsDropped_Type = Counter32
_DcxTFTPDWriteRequestsDropped_Object = MibScalar
dcxTFTPDWriteRequestsDropped = _DcxTFTPDWriteRequestsDropped_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 9, 1, 10),
    _DcxTFTPDWriteRequestsDropped_Type()
)
dcxTFTPDWriteRequestsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxTFTPDWriteRequestsDropped.setStatus("current")
_DcxTFTPDWriteRequestsFailed_Type = Counter32
_DcxTFTPDWriteRequestsFailed_Object = MibScalar
dcxTFTPDWriteRequestsFailed = _DcxTFTPDWriteRequestsFailed_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 9, 1, 11),
    _DcxTFTPDWriteRequestsFailed_Type()
)
dcxTFTPDWriteRequestsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxTFTPDWriteRequestsFailed.setStatus("current")
_DcxTFTPDWriteBytes_Type = Counter32
_DcxTFTPDWriteBytes_Object = MibScalar
dcxTFTPDWriteBytes = _DcxTFTPDWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 9, 1, 12),
    _DcxTFTPDWriteBytes_Type()
)
dcxTFTPDWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxTFTPDWriteBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-C3-TFTPD-MIB",
    **{"cmtsC3TFTPDMIB": cmtsC3TFTPDMIB,
       "dcxTFTPDObjects": dcxTFTPDObjects,
       "dcxTFTPDServerState": dcxTFTPDServerState,
       "dcxTFTPDCurrentDirectory": dcxTFTPDCurrentDirectory,
       "dcxTFTPDIpVerification": dcxTFTPDIpVerification,
       "dcxTFTPDClearCache": dcxTFTPDClearCache,
       "dcxTFTPDReadRequests": dcxTFTPDReadRequests,
       "dcxTFTPDReadRequestsDropped": dcxTFTPDReadRequestsDropped,
       "dcxTFTPDReadRequestsFailed": dcxTFTPDReadRequestsFailed,
       "dcxTFTPDReadBytes": dcxTFTPDReadBytes,
       "dcxTFTPDWriteRequests": dcxTFTPDWriteRequests,
       "dcxTFTPDWriteRequestsDropped": dcxTFTPDWriteRequestsDropped,
       "dcxTFTPDWriteRequestsFailed": dcxTFTPDWriteRequestsFailed,
       "dcxTFTPDWriteBytes": dcxTFTPDWriteBytes}
)
